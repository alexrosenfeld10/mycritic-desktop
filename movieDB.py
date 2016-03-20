#Gets one thousand movies
import random
import getMovies
##d = {'Terminator': [], 'Matrix': [], 'Kappa': []}
##print(d[random.choice(list(d.keys()))])


#random.randint(0,999)
c = {} #CRITICS
movies = getMovies.main()


for x in range(100):
    c['random_user ' + str(x)] = []
#print(c)

listOfCritics = list(c.keys())
print(listOfCritics)

for y in movies:
    for i in range(10):
        temp = random.choice(listOfCritics)
        randomrating = random.randint(0,1)
        rating = True
        if (randomrating == 0):
            rating = False
        c[temp] += (y, rating)
        movies[y] += (temp, rating)

print()
print('This is C')
print(c)

print()
print('This is D')
print(movies)

        
        
