"""
Asynchronously fetches the HTML content from the specified URL.
"""

import aiohttp
import asyncio
from pathlib import Path


async def fetch_html(url: str) -> str:
    """
    Asynchronously fetches the HTML content from the specified URL.

    Args:
        url (str): The URL to fetch HTML content from.

    Returns:
        str: The HTML content retrieved from the specified URL.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main() -> None:
    """
    An asynchronous function that fetches HTML content from a given URL and saves it to a file.
    Uses the fetch_html coroutine to retrieve the HTML content and then writes the content to a file.
    No parameters and no return type specified.
    """
    url = "https://ru.wikipedia.org/wiki/Python"
    html_content = await fetch_html(url)

    # Сохранение HTML-страницы в файл
    saved_file = Path(__file__).parent / "parser_data" / "wikipedia_page_aiohttp.html"
    with open(saved_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("HTML-страница успешно сохранена в файл 'wikipedia_page_aiohttp.html'")


if __name__ == "__main__":
    loop = asyncio.run(main())