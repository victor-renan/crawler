from dataclasses import dataclass
import json


OUT_DIR = "./out"
URLS_DIR = "./urls.txt"

@dataclass
class LegalObject:
    url: str
    nome: str
    resumo: str
    conteudo: str
    paragrafos: list[str]
    artigos: list[str]
    
    def deserialize(self) -> object:
        return json.dumps({
            "url": self.url,
            "nome": self.nome,
            "resumo": self.resumo,
            "conteudo": self.conteudo,
            "artigos": self.artigos,
            "paragrafos": self.paragrafos,
        })
