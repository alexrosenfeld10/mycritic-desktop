# takes user input movie name
# returns list of movies format [id, title, and thumbnail]

import time as t
import tmdbsimple as tmdb
tmdb.API_KEY = '3b688e8bee27473c3ed2c1caeeab204e'

name = input("Please enter a movie name: ")


def getIds(name):
    search = tmdb.Search()
    response = search.movie(query=name)
    for s in search.results:
        return s['id']


def getTitle(name):
    search = tmdb.Search()
    response = search.movie(query=name)
    for s in search.results:
        return s['title']
