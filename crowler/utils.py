from pathlib import Path
import os
import logging
import re

FILES = "files"
JSON = "json"

def path(pathtype, *args):
    TAG = "files"
    try:
        return Path(os.getcwd(), "crowler", pathtype, *args)
    except FileNotFoundError:
        logging.error("{}: The file path does not exists" % TAG)

    return Path(os.getcwd(), "crowler", "files")

def jsonpath(*args):
    return path(JSON, *args)


def listpath(*args):
    return os.listdir(path(FILES, *args))


def filepath(*args):
    return f"file://{path(FILES, *args)}"


def filename(file):
    return file.split('.')[0]

def sanitize(text):
    return re.compile('<.*?>').sub('', text).strip()

def sanitize_array(arr):
    aux = []
    for text in arr:
        aux.append(sanitize(text))
    return aux