from pathlib import Path
import crowler.utils as utils
import scrapy
import json
import re


class LegalSpider(scrapy.Spider):
    name = "legal"
    allowed_domains = ["*"]
    feed_options = {"format": "json", "indent": 4}
    filesdict = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for file in utils.listpath(self.name):
            self.filesdict[utils.filepath(self.name, file)] = utils.filename(file)
        self.start_urls = [*self.filesdict.keys()]

    def parse(self, response):
        file = f"{self.filesdict[response.url]}.json"
        with open(utils.jsonpath(self.name, file), 'w+', encoding="utf-8") as fp:
            json.dump({
                "nome" : utils.sanitize(response.xpath("//strong/small").get()),
                "data": utils.sanitize(response.xpath("//strong/small").get()),
                "resumo": utils.sanitize(response.xpath("//strong/small").get()),
                "artigos": utils.sanitize_array(response.xpath("//p[contains(., 'Art.')]").getall()),
                "paragrafos": utils.sanitize_array(response.xpath("//p[contains(., '§') or contains(., '-')]").getall()),
            }, fp)

            fp.close()
