# Cinemas

Find what going in cinema movies of St-Petersburg and show information like rating and link

### How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

### How to use
##### Sample run
```bash
$ python3 cinemas.py -w 150 -a 3
+-----------------------------+--------------------------------------+-----------+-------------+-------------------------------------+---------------+
|            Title            |             Descriprion              | KP_rating | IMDB_rating |                Link                 | Cinema_amount |
+=============================+======================================+===========+=============+=====================================+===============+
| Ван Гог. С любовью, Винсент | Конгениальная творчеству знаменитого | 8.534     | 8           | https://www.kinopoisk.ru//film/9097 | 28            |
|                             | художника анимационная картина       |           |             | 20                                  |               |
+-----------------------------+--------------------------------------+-----------+-------------+-------------------------------------+---------------+
| Дело храбрых                | Фильм-катастрофа про подвиг пожарной | 8.051     | 8.100       | https://www.kinopoisk.ru//film/9657 | 28            |
|                             | бригады                              |           |             | 54                                  |               |
+-----------------------------+--------------------------------------+-----------+-------------+-------------------------------------+---------------+
| Аритмия                     | История двух супругов-врачей,        | 7.927     | 7.700       | https://www.kinopoisk.ru//film/9926 | 12            |
|                             | которые упустили смысл своих         |           |             | 05                                  |               |
|                             | отношений                            |           |             |                                     |               |
+-----------------------------+--------------------------------------+-----------+-------------+-------------------------------------+---------------+
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
