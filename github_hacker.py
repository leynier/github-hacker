from os import system
from random import randint
from sys import argv

try:
    system('git init')
    limit = int(argv[1])
    for i in range(limit):
        message = f'{randint(0, 100000000)}'
        with open('file.txt', 'a') as file:
            file.write(message)
        system('git add .')
        system(f'git commit -m {message}')
        print(f'Iteration: {i + 1}')
        if (i + 1) % 100 == 0:
            system('git push origin master')
    system('git push origin master')
except IndexError:
    print('Limit param not found.')
except TypeError:
    print('Limit should be a integer')
