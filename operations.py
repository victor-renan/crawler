import re

def parse_url(content: str) -> str:
    return re.sub("\n", "", content).strip()

def select_first(pattern: str, content: str) -> str:
    results = re.findall(pattern, content)
    if len(results) == 0: return ""
    return results[0]

def sanitize(content: str) -> str:
    return re.sub(r"<.*?>", "", content).replace("\n", "")

def select_all(pattern: str, content: str) -> list[str]:
    return re.findall(pattern, content)

def parse_name(url: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '-', url.split("/")[-1].strip().split(".")[0])