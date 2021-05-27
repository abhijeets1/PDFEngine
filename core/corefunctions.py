from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from pdf2image import convert_from_path
from pytesseract import pytesseract
from pikepdf import Pdf, Encryption
from pdf2docx import parse
from PIL import Image
import img2pdf
import shutil
import os

# ----- common functions -----
def handle_uploaded_file(file, location):
	with open(location + '/static/upload/' + file.name, 'wb+') as destination:
		for chunk in file.chunks():
			destination.write(chunk)

# ----- pdfmerge functions -----
def merge_files(filenames, timestamp):
	pdf_files_path = 'pdfmerge/static/upload/'
	merged_file_path = 'pdfmerge/static/upload/merged/' + timestamp + '.pdf'

	merger = PdfFileMerger()
	for filename in filenames:
		merger.append(pdf_files_path + filename)
	merger.write(merged_file_path)
	merger.close()

	return timestamp + '.pdf'

# ----- pdfsplit functions -----
def split_file(file, pageno, nofpages, timestamp):
	pdf_file_path = 'pdfsplit/static/upload/' + file.name
	splited_file_name = timestamp + '.pdf'
	splited_file_path = 'pdfsplit/static/upload/splited/' + splited_file_name

	pdfreader = PdfFileReader(pdf_file_path)
	pdfwriter = PdfFileWriter()

	for no in range(nofpages):
		page = pdfreader.getPage((pageno-1)+no)
		pdfwriter.addPage(page)
	with open(splited_file_path, 'wb+') as f:
		pdfwriter.write(f)

	return splited_file_name

def validate_pdf_split(filename, pageno, nofpages):
	pdf_file_path = 'pdfsplit/static/upload/' + filename

	pdf = open(pdf_file_path, 'rb+')
	pdfreader = PdfFileReader(pdf)
	pdfpages = pdfreader.numPages
	temp = (pdfpages - pageno) + 1
	exceptions = []

	if not (pageno > 0):	
		exceptions.append('Initial page number is zero or less than 0!')
	if not (pageno <= pdfpages):
		exceptions.append('Initial page number is more than total pages!')
	if not (nofpages > 0):
		exceptions.append('Number of pages is zero or less than 0!')
	if not (temp >= nofpages):
		exceptions.append('Number of pages is off limit!')

	return exceptions

# ----- pdfencrypt functions -----
def encrypt_file(file, password, timestamp):
	pdf_file_path = 'pdfencrypt/static/upload/' + file.name
	encrypted_file_name = timestamp + '.pdf'
	encrypted_file_path = 'pdfencrypt/static/upload/encrypted/' + encrypted_file_name
	exceptions = []

	pdfreader = PdfFileReader(pdf_file_path)
	if pdfreader.isEncrypted:
		exceptions.append('PDF file is already encryted!')

	if len(exceptions) > 0:
		return ('', exceptions)
	else:
		pdf = Pdf.open(pdf_file_path)
		pdf.save(encrypted_file_path,
			encryption = Encryption(owner=password, user=password, R=6)
		)
		pdf.close()
		return (encrypted_file_name, [])

# ----- pdfdecrypt functions -----
def decrypt_file(file, password, timestamp):
	pdf_file_path = 'pdfdecrypt/static/upload/' + file.name
	decrypted_file_name = timestamp + '.pdf'
	decrypted_file_path = 'pdfdecrypt/static/upload/decrypted/' + decrypted_file_name
	exceptions = []

	pdfreader = PdfFileReader(pdf_file_path)
	if not pdfreader.isEncrypted:
		exceptions.append('PDF file is not encryted!')
	try:
		pdf = Pdf.open(pdf_file_path, password=password)
	except Exception:
		exceptions.append('Incorrect password!')

	if len(exceptions) > 0:
		return ('', exceptions)
	else:
		pdf.save(decrypted_file_path)
		return (decrypted_file_name, [])

# ----- imgtopdf functions -----
def image_to_pdf(filenames, timestamp):
	image_file_path = 'imgtopdf/static/upload/'
	topdf_file_name = timestamp + '.pdf'
	topdf_file_path = 'imgtopdf/static/upload/topdf/' + topdf_file_name
	imagenames = []

	pdffile = open(topdf_file_path, "wb+")
	for filename in filenames:
		image = Image.open(image_file_path + filename)
		image = image.convert('RGB')
		image.save(image_file_path + filename)

		image = Image.open(image_file_path + filename)
		pdf_bytes = img2pdf.convert(image.filename)
		imagenames.append(image.filename)
		image.close()

	pdffile.write(img2pdf.convert(imagenames))
	pdffile.close()

	return topdf_file_name

# ----- pdftoimg functions -----
def pdf_to_image(file, timestamp):
	pdf_file_path = 'pdftoimg/static/upload/' + file.name
	images_folder_path = 'pdftoimg/static/upload/toimg/' + timestamp
	imagepath = images_folder_path + '/'
	imagesname = []

	os.mkdir(images_folder_path)
	images = convert_from_path(pdf_file_path)
	for i in range(len(images)):
		imagename = 'page' + str(i) + '.jpg'
		images[i].save(imagepath + imagename, 'JPEG')
		imagesname.append(imagename)

	return imagesname

# ----- pdftoword functions -----
def pdf_to_word(file):
	pdf_file_path = 'pdftoword/static/upload/' + file.name
	word_file_name = file.name.replace('.pdf', '') + '.docx'
	word_file_path = 'pdftoword/static/upload/toword/' + word_file_name

	parse(pdf_file_path, word_file_path, start=0, end=None)

	return word_file_name

# ----- imgtotext functions -----
def img_to_text(file, timestamp):
	image_file_path = 'imgtotext/static/upload/' + file.name
	text_file_name = timestamp + '.txt'
	text_file_path = 'imgtotext/static/upload/totext/' + text_file_name
	# tesseract_path = 'imgtotext/Tesseract-OCR/tesseract.exe'

	img = Image.open(image_file_path)
	# pytesseract.tesseract_cmd = tesseract_path
	text = pytesseract.image_to_string(img)
	textfile = open(text_file_path , 'w+')
	textfile.write(text)

	return (text, text_file_name)

def pdf_copy_protect(filename, timestamp):
	pdf_file_path = 'pdfcprotect/static/upload/' + filename
	images_folder_path = 'pdfcprotect/static/upload/cprotected/' + timestamp
	imagepath = images_folder_path + '/'
	imagesnames = []
	cprotected_file_name = timestamp + '.pdf'
	cprotected_file_path = imagepath + cprotected_file_name

	os.mkdir(images_folder_path)
	images = convert_from_path(pdf_file_path)
	for i in range(len(images)):
		imagename = 'page' + str(i) + '.jpg'
		images[i].save(imagepath + imagename, 'JPEG')
		imagesnames.append(imagename)

	temp = []
	pdffile = open(cprotected_file_path, "wb+")
	for imagename in imagesnames:
		image = Image.open(imagepath + imagename)
		pdf_bytes = img2pdf.convert(image.filename)
		temp.append(image.filename)
		image.close()
	
	pdffile.write(img2pdf.convert(temp))
	return cprotected_file_name