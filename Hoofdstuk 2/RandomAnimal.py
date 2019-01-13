from urllib.request import urlopen
from random import randint

print("I'm going to guess your favorite animal...")
with urlopen('https://raw.githubusercontent.com/BearWithAFez/Learning-Python/master/Hoofdstuk%202/animals.txt') as webz:
    animals = []
    for animal in webz:
        animals.append(animal.decode('utf-8').rstrip())

print('*** The ' + animals[randint(0, len(animals))] + ' ***')
print('Am I right? :D')
