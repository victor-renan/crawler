from operations import *
from domain import *
import requests

def build() -> None:
    for url in open(SEGES_URLS).readlines():
        parsed_url = parse_url(url)
        filename = purify(parse_name(parsed_url))

        if bool(parsed_url):
            res = requests.get(parsed_url)
            articles = select_first(r'<div id="parent-fieldname-text">(.*?)</div>', purify(res.text, False))
            split_article = '>Art.' + articles.split('>Art.', 1)[-1]

            legal_object = LegalObject(
                url = parsed_url,
                nome = purify(select_first(r'>(.*?)</h1>', res.text)),
                resumo = purify(select_first(r'<div class="documentDescription description">(.*?)</div>', res.text)),
                conteudo = select_till(purify(split_article)[1::], 200),
                paragrafos = purify_all(select_all(r'>(.*?)</p>', split_article)),
            )

            create_file(make_file(filename, "json"), legal_object)