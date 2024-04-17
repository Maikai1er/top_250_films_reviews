from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) '
                  'Chrome/80.0.3987.162 Safari/537.36'}


top_actors = {}


def process_link(link):
    html = requests.get(link, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    actors = soup.find_all(class_='ipc-lockup-overlay ipc-focusable', href=lambda href: href and '/name/' in href)
    actor_names = [actor['aria-label'] for actor in actors]
    for actor_name in actor_names:
        if actor_name not in top_actors:
            top_actors[actor_name] = 1
        else:
            top_actors[actor_name] += 1
    # print(actor_names)


def run():
    url = "https://www.imdb.com/chart/top/"
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.find_all(class_='ipc-title-link-wrapper')
    website = urlparse(url)
    end_links = [f'{website.scheme}://{website.netloc}{link['href']}' for link in links if 'ql' not in link['href']]
    i = 0
    for link in end_links:
        print(f'Processing {link}')
        process_link(link)
        i += 1
        if i == 10:
            break
    print(top_actors)
    with open('top_actors.txt', 'w', encoding='utf-8') as file:
        for actor, count in top_actors.items():
            file.write(f'{actor}: {count}\n')
    # print(end_links)
