# Cinemas

Find what going St-Petersburg cinemas and show information about movies

### How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

### How to use
##### Sample run
```bash
$ python3 cinemas.py -w 100 -a 3 -m 30
+------------------+------------------+-----------+-------------+------------------+---------------+
|      Title       |   Descriprion    | KP_rating | IMDB_rating |       Link       | Cinema_amount |
+==================+==================+===========+=============+==================+===============+
| Тор: Рагнарек    | Тор и Халк       | 7.761     | 8.200       | https://www.kino | 106           |
|                  | против богини    |           |             | poisk.ru//film/8 |               |
|                  | смерти           |           |             | 22709            |               |
+------------------+------------------+-----------+-------------+------------------+---------------+
| Последний        | Второй           | 7.146     | 7           | https://www.kino | 55            |
| богатырь         | полнометражный   |           |             | poisk.ru//film/9 |               |
|                  | фильм студии     |           |             | 7664             |               |
|                  | Disney в России  |           |             |                  |               |
+------------------+------------------+-----------+-------------+------------------+---------------+
| Убийство в       | Звездная         | 6.909     | 6.700       | https://www.kino | 38            |
| Восточном        | экранизация      |           |             | poisk.ru//film/8 |               |
| экспрессе        | романа Агаты     |           |             | 17969            |               |
|                  | Кристи с         |           |             |                  |               |
|                  | Кеннетом Браной  |           |             |                  |               |
|                  | в роли Эркюля    |           |             |                  |               |
|                  | Пуаро с          |           |             |                  |               |
|                  | невероятными     |           |             |                  |               |
|                  | усами            |           |             |                  |               |
+------------------+------------------+-----------+-------------+------------------+---------------+
```

##### Arguments
```bash
optional arguments:
  -h, --help            show this help message and exit
  --films_amount FILMS_AMOUNT, -a FILMS_AMOUNT
                        Number of movies to show
  --min_cinema_threshold MIN_CINEMA_THRESHOLD, -m MIN_CINEMA_THRESHOLD
                        Minimum number of cinemas to show movie
  --screen_width SCREEN_WIDTH, -w SCREEN_WIDTH
                        Screen width in chars
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
