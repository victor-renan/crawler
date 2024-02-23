from operations import *
from domain import *
import requests

def build() -> None:
    for url in open(CAMARA_URLS).readlines():
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
                paragrafos = convert_nbsp(purify(split_article).split(pattern)),
            )

            create_file(make_file(filename, "json"), legal_object)