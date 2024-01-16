
import re

def sanitize(text):
    return(
        re.compile('<.*?>')
        .sub('', text)
        .replace('/r', '')
        .replace('/n', '')
        .strip()
    )

def sanitize_array(arr):
    aux = []
    for text in arr:
        aux.append(sanitize(text))
    return aux

def resume(text, size):
    if len(text) <= size:
        return text

    return text[0:size-4] + "..."