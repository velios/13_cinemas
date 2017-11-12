from argparse import ArgumentParser
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial

import requests
from bs4 import BeautifulSoup
from texttable import Texttable


def make_cmd_arguments_parser():
    parser_description = 'Script find info for going in cinema movies'
    parser = ArgumentParser(description=parser_description)
    parser.add_argument('--films_amount', '-a',
                        help='Number of movies to show',
                        type=int,
                        default=10)
    parser.add_argument('--min_cinema_threshold', '-m',
                        help='Minimum number of cinemas to show movie',
                        type=int,
                        default=10)
    parser.add_argument('--screen_width', '-w',
                        help='Screen width in chars',
                        type=int,
                        default=80)
    return parser.parse_args()


def fetch_proxy_list():
    freeproxy_url = 'http://www.freeproxy-list.ru/api/proxy'
    response = requests.get(freeproxy_url, params={'anonymity': 'false', 'token': 'demo'})
    return response.text.split()


def parse_afisha_list():
    afisha_url = 'https://www.afisha.ru/spb/schedule_cinema/'
    raw_afisha_html = requests.get(afisha_url).content

    soup = BeautifulSoup(raw_afisha_html, "html.parser")
    movie_tag_list = soup.find('div', id='schedule').find_all('div', recursive=False)

    movie_data_list = []
    for movie in movie_tag_list:
            movie_content_tag = movie.find('div', {'class': 'm-disp-table'})
            movie_title = movie_content_tag.find('a').text
            movie_description = movie_content_tag.find('p').text
            cinema_list = movie.find('tbody').find_all('tr', recursive=False)
            movie_data_list.append({
                'title': movie_title,
                'description': movie_description,
                'cinema_amount': len(cinema_list)
            })
    return movie_data_list


def _fetch_movie_rating(kinopoisk_movie_id):
    movie_rating_url = 'https://rating.kinopoisk.ru/{id}.xml'.format(id=kinopoisk_movie_id)
    raw_rating_xml = requests.get(movie_rating_url).content

    soup = BeautifulSoup(raw_rating_xml, "xml")
    kp_data = soup.find('kp_rating')
    imdb_data = soup.find('imdb_rating')
    rating_dict = {}
    if kp_data:
        rating_dict.update({
            'kp_rating': kp_data.text,
            'kp_votes': kp_data.attrs['num_vote']
        })
    if imdb_data:
        rating_dict.update({
            'imdb_rating': imdb_data.text,
            'imdb_votes': imdb_data.attrs['num_vote']
        })
    return rating_dict


def fetch_kinopoisk_movie_info(movie_title):
    search_url = 'https://www.kinopoisk.ru/search/suggest'
    search_params = {'q': movie_title, 'topsuggest': 'true', 'ajax': '1'}
    search_response = requests.get(
        search_url,
        params=search_params,
    )
    movie_data_dict = search_response.json()[0]
    movie_kinopoisk_id = movie_data_dict['id']
    movie_data_dict.update(_fetch_movie_rating(movie_kinopoisk_id))
    return movie_data_dict


def output_movies_to_console(movies_data, screen_width=80):
    table = Texttable(max_width=screen_width)
    table_head = [['Title', 'Descriprion', 'KP_rating', 'IMDB_rating', 'Link', 'Cinema_amount']]
    body_keys = ['title', 'description', 'kp_rating', 'imdb_rating', 'link', 'cinema_amount']
    table_body = []
    for movie in movies_data:
        movie['link'] = ('https://www.kinopoisk.ru/{link}'.format(link=movie['link'])).rstrip('/sr/2/')
        table_body.append([movie.get(key) for key in body_keys])
    table.add_rows(table_head + table_body)
    print(table.draw())


def thread_update_movie_info(movie, min_cinema_threshold):
    if movie['cinema_amount'] >= min_cinema_threshold:
        movie.update(fetch_kinopoisk_movie_info(movie['title']))
        return movie
    else:
        return None


if __name__ == '__main__':
    cmd_arguments = make_cmd_arguments_parser()
    films_amount = cmd_arguments.films_amount
    min_cinema_threshold = cmd_arguments.min_cinema_threshold
    screen_width = cmd_arguments.screen_width
    try:
        ongoing_movies_list = parse_afisha_list()

        pool = ThreadPool(8)
        full_movies_data_list = pool.map(partial(thread_update_movie_info,
                                                 min_cinema_threshold=min_cinema_threshold),
                                         ongoing_movies_list)
        full_movies_data_list = [movie for movie in full_movies_data_list if movie]
        full_movies_data_list.sort(key=lambda k: k['kp_rating'], reverse=True)
        output_movies_to_console(
            movies_data=full_movies_data_list[:films_amount],
            screen_width=screen_width
        )
    except requests.exceptions.ConnectionError as e:
        print('Connection problem')
