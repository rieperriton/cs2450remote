
 ###this is my file

import random

print('Hello! I am going to guess your age')
user_name = input('What is your name? ')

while True:
    guess = random.randrange(15, 30)

    print(f'Is your age {guess}')

    correct = input('Correct? (y/n) ')

    if correct == 'y':
        print(f'{user_name} is {guess} years old!')
        break

    else:
        print('Rats. I will guess again')

feedback = input('Did you enjoy this? (y/n')
##what a god awful program i wrote here 


