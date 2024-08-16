import sqlite3
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
    directors: list[str]
    year: int
    description: str
    countries: list[str]
    movie_link: str  
    img_link: str
    age_restrictions: int


def main() -> None:
    movies = []

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

        response = requests.get(movie_link, headers=headers)
        if response.status_code != 200:
            print("Не смог получить страницу!")
            return

        soup_card = BeautifulSoup(response.text, "lxml")

        # genres = [genre.text for genre in soup_card.find_all("span", class_="badge__text")]
        genres = []
        for genre in soup_card.find_all("span", class_="badge__text"):
            genres.append(genre.text)

        datas = soup_card.find("div", class_="p-movie-info__content").find("div", class_="p-columns") \
            .find_all("div", {"class": [
            "table",
            "table_layout_fixed",
            "p-columns__item"
        ]})

        directors_data = datas[0].find_all("div", class_="table__cell")[-1].find_all("a")
        directors = []
        for director_data in directors_data:
            directors.append(director_data.text)

        actors_data = datas[1].find_all("div", class_="table__cell")[-1].find_all("a")
        actors = []
        for actor_data in actors_data:
            actors.append(actor_data.text)

        countries_data = datas[2].find_all("div", class_="table__cell")[-1].find_all("a")
        countries = []
        for country_data in countries_data:
            countries.append(country_data.text)

        age_restrictions = datas[3].find_all("div", class_="table__cell")[-1].text.split(" ")[0]
        # print(soup_card.find("div", class_="p-movie-info__content").find("div", class_="margin_bottom_20"))
        try:
            year = int(soup_card.find("div", class_="p-movie-info__content") \
                       .find("div", class_="margin_bottom_20")
                       .find("span").find("a").text)
        except ValueError:
            year_data = soup_card.find("div", class_="p-movie-info__content").find_all("a", class_="color_black")

            year = None
            exist_year = False
            for i in year_data:
                if "/cinema/all/" in i["href"] and not exist_year:
                    year = int(i.text)
                    exist_year = True

        img_link = soup_card.find("picture", {"class": ["picture", "p-framer__picture"]}).find("img")["src"]
        description = soup_card.find("div", class_="p-movie-info__description").find("p").text

        movies.append((
            movie_name,
            ", ".join(genres),
            ", ".join(actors),
            ", ".join(directors),
            year,
            description,
            ", ".join(countries),
            movie_link,
            img_link,
            age_restrictions,
        ))

    # print(movies)



    conn = sqlite3.connect("mydata.db")

    cursor = conn.cursor()

    cursor.executemany("INSERT INTO films VALUES (?,?,?,?,?,?,?,?,?,?)", movies)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
