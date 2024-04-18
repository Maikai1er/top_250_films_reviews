from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) '
                  'Chrome/80.0.3987.162 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}


class Actor:
    def __init__(self, name):
        self.name = name
        self.films_count = 0
        self.films = []

    def __str__(self):
        return f'{self.name}. Starred in {self.films_count} films. Films are: {self.films}'

    def get_actor_name(self):
        return self.name

    def increase_films_count(self):
        self.films_count += 1

    def add_film(self, film):
        self.films.append(film)

    def get_films_count(self):
        return self.films_count

    def get_films(self):
        return self.films


top_actors = {}


def process_link(link):
    html = requests.get(link, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    film_name = soup.find(class_='hero__primary-text').text
    actors = soup.find_all(class_='ipc-lockup-overlay ipc-focusable', href=lambda href: href and '/name/' in href)
    for actor in actors:
        actor_name = actor['aria-label'].strip()
        if actor_name not in top_actors:
            new_actor = Actor(actor_name)
            new_actor.increase_films_count()
            new_actor.add_film(film_name)
            top_actors[actor_name] = new_actor
        else:
            existing_actor = top_actors[actor_name]
            existing_actor.increase_films_count()
            existing_actor.add_film(film_name)


def get_top_actors():
    url = "https://www.imdb.com/chart/top/"
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.find_all(class_='ipc-title-link-wrapper')
    website = urlparse(url)
    film_links = [f'{website.scheme}://{website.netloc}{link['href']}' for link in links if 'ql' not in link['href']]
    for link in film_links:
        print(f'Processing {link}')
        process_link(link)
    return top_actors


def sort_top_actors(top_actors):
    return sorted(top_actors.items(), key=lambda item: (-item[1].films_count, item[0]))


def write_top_actors_to_file(filename, actors_list):
    with open(filename, 'w', encoding='utf-8') as file:
        for actor_name, actor_obj in actors_list:
            file.write(f"{'-'*30}\n")
            file.write(f"Name: {actor_obj.get_actor_name()}\n")
            file.write(f"Films Count: {actor_obj.get_films_count()}\n")
            file.write("Films:\n")
            for film in actor_obj.get_films():
                file.write(f"- {film}\n")
