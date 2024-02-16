from operations import *
from domain import LegalObject, OUT_DIR, URLS_DIR
from dataclasses import dataclass
from os import path
import requests
import re


def create_file(filename: str, content: LegalObject) -> None:
    with open(path.join(OUT_DIR, filename), "w+") as fr:
        fr.write(content.deserialize())
        fr.close()

def build_requests() -> None:
    for url in open(URLS_DIR).readlines():
        parsed_url = parse_url(url)
        filename = purify(parse_name(parsed_url))

        if bool(parsed_url):
            res = requests.get(parsed_url)
            pattern = "&nbsp;&nbsp;&nbsp;&nbsp;"
            split_article = ("Art. 1" + purify(res.text.split("Art. 1", 1)[-1], False))
            legal_object = LegalObject(
                url = parsed_url,
                nome = purify(select_first(r"<h1>.*</h1>", res.text)),
                resumo = purify(select_first(r'<p class="ementa">(.*?)</p>', purify(res.text, False))),
                conteudo = convert_nbsp([select_till(purify(split_article), 200)])[0],
                artigos = convert_nbsp(purify(split_article).split(pattern)),
                paragrafos = convert_nbsp(purify(split_article).split(pattern)),
            )

            create_file(make_file(filename, "json"), legal_object)

build_requests()
