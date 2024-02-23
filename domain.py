from dataclasses import dataclass
import json


OUT_DIR = "./out"
CAMARA_URLS = "./in/camara.txt"
SEGES_URLS = "./in/seges.txt"

@dataclass
class LegalObject:
    url: str
    nome: str
    resumo: str
    conteudo: str
    paragrafos: list[str]
    
    def deserialize(self) -> object:
        return json.dumps({
            "url": self.url,
            "nome": self.nome,
            "resumo": self.resumo,
            "conteudo": self.conteudo,
            "paragrafos": self.paragrafos,
        })
