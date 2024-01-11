from pathlib import Path
import crowler.utils as utils
import scrapy
import json
from datetime import datetime


class LegislationSpider(scrapy.Spider):
    name = "legislation"
    allowed_domains = ["www2.camara.leg.br"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [kwargs.get('url', None)]
        self.filepath = kwargs.get('path', None)
        self.filename = kwargs.get('name', None)

    def parse(self, response):
        with open(Path(self.filepath, f"{self.filename}.json"), 'w+') as fp:
            json.dump({
                "nome" : utils.sanitize(response.xpath("//div[@id='content']/h1").get()),
                "data": utils.sanitize(response.xpath("//div[@id='content']/h1").get().split(',')[1][4::]).capitalize(),
                "resumo": utils.sanitize(response.xpath("//p[@class='ementa']").get()),
                "paragrafos": utils.sanitize_array(response.xpath("//div[@class='texto']").get().split('<br><br>')),
                "artigos": utils.sanitize_array(response.xpath("//div[@class='texto']").get().split('<br><br>')),
            }, fp)

            fp.close()
