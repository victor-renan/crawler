# Crowler de Dados

Para executar este crowler, faça o seguinte:

1. Clone o repo e crie um ambiente virtual

```zsh
git clone https://github.com/victor-renan/crowler
cd crowler

# Crie um ambiente virtual
# No Ubuntu ou Debian, use python3
python -m venv .venv
```

2. Ative o ambiente:
Linux:
```zsh
source .venv/bin/activate
```
Windows:
```powershell
./.venv/Stripts/Activate.ps1
```

3. Instale as dependencias
```zsh
pip install -r requirements.txt
```

4. Baixe as páginas html da legislação e coloque na pasta crowler/files/legal

5. Execute
```zsh
scrapy crawl legal
```