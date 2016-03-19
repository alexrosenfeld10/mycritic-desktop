
from collections import OrderedDict

D = {}

movies = ["Terminator", "Matrix", "Forrest Gump", "Titanic"]

person1 = ["Jake", ("Terminator", False), ("Matrix", False), \
           ("Forrest Gump", True)]

person2 = ["Will", ("Terminator", True), ("Matrix", True),\
           ("Forrest Gump", False), ("Titanic", False)]

person3 = ["Alex", ("Terminator", False), ("Matrix", True),\
           ("Forrest Gump", True), ("Titanic", True)]

person4 = ["Mark", [("Matrix", True), ("Titanic", True)]]

people = [person1, person2, person3]

for i in range(len(movies)):
    D[movies[i]] = []

for j in people:
    ts = j[1:]
    for k in ts:
        D[k[0]] += [(j[0], k[1])]

print(D)

sentiment_Table = {}
person4movies = person4[1]
for k in person4movies:
    temp_people = D[k[0]]
    for L in temp_people:
           print(L[0])
           if L[0] not in sentiment_Table:
               if L[1] == k[1]:
                   sentiment_Table[L[0]] = 1
               else:
                   sentiment_Table[L[0]] = -1
           else:
                if L[1] == k[1]:
                    sentiment_Table[L[0]] += 1
                else:
                    sentiment_Table[L[0]] += -1
        
        
print(sentiment_Table)

check_movie = input("Input a movie to check: ")

def getScoreForMovie(movie):
    sentiment = 0
    abs_sentiment = 0
    count = 0
    for k in D[movie]:
        if k[0] in sentiment_Table:
            sentiment += sentiment_Table[k[0]]
            abs_sentiment += abs(sentiment_Table[k[0]])
            count += int(k[1]) * 100
            #check_table += [(sentiment_Table[k[0]], k[1])]
        else:
            #check_table += [(0, k[1])]
            count += int(k[1]) * 100

    tf_average = count / len(D[movie])
    weight = sentiment/abs_sentiment
    if weight > 0:
        diff = 100 - tf_average
        tf_average += diff * weight
    else:
        diff = tf_average
        tf_average -= diff * weight
    print(tf_average)

getScoreForMovie(check_movie)



#for movie in D:
#    for tup in movie:
#        if tup[1] == True and person4[
#        new_user += [(tup[0], )]
