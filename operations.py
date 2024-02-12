import re

def parse_url(content: str) -> str:
    return re.sub("\n", "", content).strip()

def select_first(pattern: str, content: str) -> str:
    results = re.findall(pattern, content)
    if len(results) == 0: return ""
    return results[0]

def purify(content: str) -> str:
    return (
        re.sub(r"<.*?>", "", content)
        .replace("\n", "")
        .replace("\r", "")
        .replace("\t", "")
        .strip()
    )

def purify_all(content: list) -> list:
    aux = []
    for item in content:
        aux.append(sanitize(item))
    return aux

def select_all(pattern: str, content: str) -> list[str]:
    return re.findall(pattern, content)

def parse_name(url: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '-', url.split("/")[-1].strip().split(".")[0])

def make_file(name: str, ext: str) -> str:
    return f"{name}.{ext}"