from dataclasses import dataclass

import requests

from pprint import pprint
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()


# def get_cards_


@dataclass(frozen=True)
class Movie:
    name: str
    genres: list[str]
    actors: list[str]
    director: list[str]
    year: int
    description: str
    country: str
    movie_link: str
    img_link: str


def main() -> None:
    url = "https://kino.mail.ru/cinema/all/"
    headers = {"User-Agent": ua.random}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Не смог получить страницу!")
        return

    soup = BeautifulSoup(response.text, "lxml")

    cards = soup.find_all("div", {"class": [
        "cols__column",
        "cols__column_small_percent-100",
        "cols__column_medium_percent-50",
        "cols__column_large_percent-50"
    ]
    })

    data = []
    for c, card in enumerate(cards):
        if c == 1:
            continue

        try:
            movie_name = card.find("div", class_="cols__inner").find("div", class_="p-itemevent-small__info") \
                .find("span", class_="link__text").text
            movie_link = "https://kino.mail.ru" + card.find("div", class_="cols__inner") \
                .find("div", class_="p-itemevent-small__info").find("a", class_="link")["href"]
        except AttributeError:
            continue
        print(movie_name)


if __name__ == "__main__":
    main()