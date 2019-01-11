from random import randint

print('I will say a number between 0 and 10')
print('Say -H- When the next number will be higher.')
print('Say -L- When it will be lower.')
print('Say -S- to make me stop!')

number = randint(0, 10)
nxtNumber = 0
points = 0
while True:
    print('Current score: ' + str(points))
    print('The current number is ' + str(number) + ', what will it be?')
    x = input()

    if x == 'S':
        break

    if x == 'H':
        nxtNumber = randint(0, 10)
        print('So is ' + str(nxtNumber) + ' bigger than ' + str(number) + '?')

        if number < nxtNumber:
            points += 1
            print("Yep! (+1)")
        else:
            points -= 1
            print("Nope! (-1)")

        number = nxtNumber

    if x == 'L':
        nxtNumber = randint(0, 10)
        print('So is ' + str(nxtNumber) + ' smaller than ' + str(number) + '?')

        if number > nxtNumber:
            points += 1
            print("Yep! (+1)")
        else:
            points -= 1
            print("Nope! (-1)")

        number = nxtNumber

print('Thank you for playing!')
