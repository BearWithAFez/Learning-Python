from random import randint
print('Please type in every single option one line at a time. then proceed to type "CHOOSE" to get help')

options = []
while True:
    inp = input()

    if inp == 'CHOOSE':
        break

    options.append(inp)
    print('There are ' + str(len(options)) + ' in, whats the next?')

if len(options) != 0:
    print(options[randint(0, len(options)-1)])

print('Thank you for using me!')
