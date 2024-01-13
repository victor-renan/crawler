from pathlib import Path
import crowler.utils as utils
import scrapy
import json


class LegislationSpider(scrapy.Spider):
    name = "legislation"
    allowed_domains = ["www2.camara.leg.br"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [str(kwargs.get('url', None))]
        self.url = str(kwargs.get('url', None))
        self.filepath = str(kwargs.get('path', None))
        self.filename = str(kwargs.get('name', None))

    def parse(self, response):
        with open(Path(self.filepath, f"{self.filename}.json"), 'w+') as fp:
            json.dump({
                "url": self.url,
                "nome" : utils.sanitize(response.xpath("//div[@id='content']/h1").get()),
                "data": utils.sanitize(response.xpath("//div[@id='content']/h1").get()).split(',')[1][4::].capitalize(),
                "resumo": utils.resume(utils.sanitize(response.xpath("//p[@class='ementa']").get()), 52),
                "paragrafos": utils.sanitize_array(response.xpath("//div[@class='texto']").get().split('<br><br>')),
                "artigos": utils.sanitize_array(response.xpath("//div[@class='texto']").get().split('<br><br>')),
                "conteudo": "Art" + utils.resume(utils.sanitize(response.xpath("//div[@class='texto']").get())
                                                 .split("Art", 1)[1], 150).replace('\u00a0\u00a0\u00a0\u00a0\u00a0', ''),
            }, fp)

            fp.close()
