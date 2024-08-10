from os import read
from bs4 import BeautifulSoup
from pathlib import Path

if __name__ == "__main__":
    # Открываем файл с HTML-кодом страницы

    reading_file = (
        Path(__file__).parent / "parser_data" / "wikipedia_page_aiohttp.html"
    )
    with open(reading_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Находим первый абзац
    first_paragraph = soup.find("p")

    print("Первый абзац с сайта Википедии:")
    print(first_paragraph.text)