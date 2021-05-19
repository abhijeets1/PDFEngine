from django import template
from django.utils.html import mark_safe
import re

register = template.Library()

def highlight_search(text, search):
	highlighted = text.replace(search, '<mark class="alert alert-success p-1">{}</mark>'.format(search))
	return mark_safe(highlighted)

def multiple_replace(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in sorted(rep_dict,key=len,reverse=True)]), flags=re.DOTALL)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

def highlight_all_search(text, search):
	dict = {}
	for item in search:
		dict[item] = '<mark class="alert alert-success p-1">{}</mark>'.format(item)
	
	text = multiple_replace(text, dict)
	return mark_safe(text)

register.filter('highlight_search', highlight_search)
register.filter('highlight_all_search', highlight_all_search)