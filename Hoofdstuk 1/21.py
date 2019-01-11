from random import randint
print('Let\'s play blackjack!')
print('Say -hit- when you want me to deal you the next card.')
print('Say -fold- when to fold.')
print('Say -S- to make me stop!')
print('You get a point for every point above 13.')

points = 0
stack = 0
while True:
    print('Current score: ' + str(points))

    if stack == 0:
        stack = randint(1,13)
        print('let\'s start it off with a ' + str(stack))

    print('The current stack is worth ' + str(stack) + ', what will it be?')
    x = input()

    if x == 'S':
        break

    if x == 'hit':
        number = randint(1, 13)
        print('Next hit: ' + str(number))

        if (number + stack) > 21:
            print("Ouch! Overshot it by " + str(number + stack - 21))
            points -= (number + stack - 21)
            stack = 0

        elif (number + stack) == 21:
            print("WOW NICE!")
            points += (number + stack - 13)
        else:
            print("Okay lets add it to the stack")
            stack += number

    if x == 'fold':
        print('Playing it safe?')
        points += stack - 13
        stack = 0

print('Thank you for playing!')
