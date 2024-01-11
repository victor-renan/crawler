
import re

def sanitize(text):
    return re.compile('<.*?>').sub('', text).strip()

def sanitize_array(arr):
    aux = []
    for text in arr:
        aux.append(sanitize(text))
    return aux