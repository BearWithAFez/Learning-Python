from random import randint

print('let\'s play Rock Paper Scissors!')
print('You know how it works, just say -R- -P- or -S- respectively.')
print('Say -STOP- to stop the game.')

number = randint(0, 2)
points = 0
while True:
    print('*** Current score: ' + str(points) + ' ***')
    print('Alright 3- 2- 1- GO!')
    x = input()

    if x == 'STOP':
        break

    if x == 'S':
        if number == 0:
            print('ROCK!')
            print('My point! (-1)')
            points -= 1
        elif number == 1:
            print('PAPER!')
            print('Your point! (+1)')
            points += 1
        else:
            print('SCISSORS!')
            print('Stalemate... (no points)')

    elif x == 'R':
        if number == 0:
            print('ROCK!')
            print('Stalemate... (no points)')
        elif number == 1:
            print('PAPER!')
            print('My point! (-1)')
            points -= 1
        else:
            print('SCISSORS!')
            print('Your point! (+1)')
            points += 1

    elif x == 'P':
        if number == 0:
            print('ROCK!')
            print('Your point! (+1)')
            points += 1
        elif number == 1:
            print('PAPER!')
            print('Stalemate... (no points)')
        else:
            print('SCISSORS!')
            print('My point! (-1)')
            points -= 1
    else:
        print("That\'s not a valid answer... say -R- -P- or -S-!")
    number = randint(0, 2)

print('Thank you for playing!')
