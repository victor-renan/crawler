from operations import *
from domain import LegalObject, OUT_DIR, URLS_DIR
from dataclasses import dataclass
from os import path
import requests
import re


def create_file(filename: str, content: LegalObject) -> None:
    with open(path(OUT_DIR, filename), "w+") as fr:
        fr.write(json.dumps(content))
        fr.close()

def build_requests() -> None:
    for url in open(URLS_DIR).readlines():

        parsed_url = parse_url(url)

        if bool(parsed_url):
            res = requests.get(parsed_url)

            print(sanitize_all(res.text.split("<BR><BR>")))

            legal_object = LegalObject(
                url = parsed_url,
                name = sanitize(parse_name(parsed_url)),
                resumo = sanitize(select_first("<h1>.*</h1>", res.text)),
                paragrafos = ["asdf"],
                artigos = ["asdf"],
            )

            print(legal_object.deserialize())


build_requests()
