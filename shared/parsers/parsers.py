import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def generate_headers() -> dict[str, str]:
    ua = UserAgent(platforms="desktop")
    headers = {
        "User-Agent": ua.random,
    }
    return headers


def parse_mmcs(url: str, filename: str = "adm") -> None:
    headers = generate_headers()
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.find("div", {"class": "newsitem_text"})
    concatenated = ""
    for item in div:
        if item.name == "h3" or item.name == "h4" or item.name == "h2" or item.name == "h5" or item.name == "h6":
            concatenated += "\n"
        if item.text is not None and item.text != "" and len(item.text) > 5:
            concatenated += f" {item.text}"
    with open(f"./data/{filename}.md", 'w') as file:
        file.write(concatenated)
