print('Think of a number 1-100')
user_input = input('Press "Enter" to start')

min_number = 1
max_number = 100

import random

while user_input != '=':
    if min_number != max_number:
        guess_number = random.randint(min_number, max_number)
    else:
        print(f'Your number is {min_number}!')
        break
    print(f'Your number is {guess_number}')
    user_input = input('Right? (=, t<, t>) ')
    if user_input == 't<':
        max_number = guess_number - 1
    elif user_input == 't>':
        min_number = guess_number + 1

print('This is Victory')
