from collections import namedtuple, defaultdict
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def fetch_html(url):
    request = requests.get(url)
    return request.content


def parse_afisha_list(raw_html):
    AfishaMovieData = namedtuple('AfishaMovieData', ['title', 'description', 'cinema_amount'])
    soup = BeautifulSoup(raw_html, "html5lib")
    movie_list = soup.find('div', id='schedule').find_all('div', recursive=False)
    
    parsed_movie_data_list = []
    for movie in movie_list:
            movie_display_tag = movie.find('div', {'class': 'm-disp-table'})
            movie_title = movie_display_tag.find('a').text
            movie_description = movie_display_tag.find('p').text
            cinema_list = movie.find('tbody').find_all('tr', recursive=False)
            parsed_movie_data_list.append({
                'title': movie_title,
                'description': movie_description,
                'cinema_amount': len(cinema_list)
            })
    return parsed_movie_data_list


def fetch_movie_info(movie_title):
    user_agent = UserAgent()
    search_url = 'https://www.kinopoisk.ru/search/suggest'
    search_params = {'q': movie_title, 'topsuggest': 'true', 'ajax': '1'}
    search_response = requests.get(
        search_url,
        params=search_params,
    )
    movie_data_dict = search_response.json()[0]
    movie_page_url = 'https://www.kinopoisk.ru{}'.format(movie_data_dict['link'])
    headers = {'User-Agent': user_agent.random}
    r = requests.get('https://www.kinopoisk.ru/film/822709/sr/2/', headers=headers)
    
    
    raw_movie_page_html = fetch_html(movie_page_url)
    soup = BeautifulSoup(raw_movie_page_html, "html5lib")
    movie_rating_full = soup.find('span', {'class': 'rating_ball'})
    # movie_votes_amount = soup.find('span', {'class': 'ratingCount'}).text
    # movie_data_dict.update([movie_rating_full, movie_votes_amount])
    
    
    # return movie_data_dict
    return r.text
    

def output_movies_to_console(movies):
    pass


if __name__ == '__main__':
    ua = UserAgent()
    afisha_url = 'https://www.afisha.ru/spb/schedule_cinema/'
    raw_afisha_html = fetch_html(afisha_url)
    parsed_afisha_data = parse_afisha_list(raw_afisha_html)
    item = parsed_afisha_data[0]
    # item.update(fetch_movie_info(item['title']))
    # print(item)
    print(fetch_movie_info(item['title']))
