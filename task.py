"""
Loads an HTML page
"""

from pathlib import Path

# import requests
from utilites.fetch_utilites import fetch_html
from utilites.path_utilites import check_path


def fetch_html(url):
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}")
    return response.text


def check_path(path: Path) -> None:
    if not path.exists():
        path.mkdir()

    if not path.is_dir():
        raise NotADirectoryError


def main() -> None:
    url = "https://ru.wikipedia.org/wiki/Python"
    try:
        response = fetch_html(url)
    except Exception as e:
        print("Произошла ошибка:", e)
        return

    if response is not None:
        saved_path = Path(__file__).parent / "parser_data"
        file_name = "wikipedia_page_requests.html"

        try:
            check_path(saved_path)
        except NotADirectoryError:
            print("Путь не является директорией")
            return

        saved_file = saved_path / file_name

        with open(saved_file, "w", encoding="utf-8") as f:
            f.write(response)

        print("HTML-страница успешно сохранена в файл 'wikipedia_page_requests.html'")
    else:
        print("Ошибка при загрузке HTML-страницы:", response.status_code)


if __name__ == "__main__":
    main()