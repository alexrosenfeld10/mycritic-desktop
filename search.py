# takes user input movie name
# returns list of movies format [id, title, and thumbnail]

import time as t
import tmdbsimple as tmdb
tmdb.API_KEY = '3b688e8bee27473c3ed2c1caeeab204e'



def getInfo(s):
    l = []
    for e in s.results:
        l += [[e['id'], e['title'], e['poster_path']]]
    return l
    
def main(string):
    results = []
    search = tmdb.Search()
    response = search.movie(query=string)
    return getInfo(search)
