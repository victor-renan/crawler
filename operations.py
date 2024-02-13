import re

def parse_url(content: str) -> str:
    return re.sub("\n", "", content).strip()

def select_first(pattern: str, content: str) -> str:
    results = re.findall(pattern, content)
    if len(results) == 0: return ""
    return results[0]

def purify(content: str, escape_html: bool = True) -> str:
    purified = content

    if (escape_html):
        purified = re.sub(r"<.*?>", "", purified)

    return (
        purified.replace("\n", "")
        .replace("\r", "")
        .replace("\t", "")
        .strip()
    )

def purify_all(content: list, escape_html: bool = True) -> list:
    aux = []
    for item in content:
        aux.append(sanitize(item, escape_html))
    return aux

def select_all(pattern: str, content: str) -> list[str]:
    return re.findall(pattern, content)

def parse_name(url: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '-', url.split("/")[-1].strip().split(".")[0])

def make_file(name: str, ext: str) -> str:
    return f"{name}.{ext}"