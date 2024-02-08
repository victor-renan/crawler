from dataclasses import dataclass
import json


OUT_DIR = "./out"
URLS_DIR = "./urls.txt"

@dataclass
class LegalObject:
    url: str
    name: str
    resumo: str
    paragrafos: list[str]
    artigos: list[str]
    
    def deserialize(self) -> object:
        return json.dumps({
            "url": self.url,
            "name": self.name,
            "resumo": self.resumo,
            "paragrafos": self.paragrafos,
            "artigos": self.artigos,
        })