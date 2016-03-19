# gets top 1000 movies
import time as t
import tmdbsimple as tmdb
tmdb.API_KEY = '3b688e8bee27473c3ed2c1caeeab204e'


movies = {}
for j in range(1,40):
    temp = tmdb.Movies(tmdb).popular(**{'page': j})['results']
    for i in temp:
        movies[i['title']] = []
t.sleep(12)
for j in range(40,51):
    temp = tmdb.Movies(tmdb).popular(**{'page': j})['results']
    for i in temp:
        movies[i['title']] = []

