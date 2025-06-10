import random
import sys

print('A random number has been chosen, can you guess what it is?')

random_num: int = random.randint(1,100)

while True:
    try:
        user_guess: int = int(input('Guess the random number: '))
        
        if user_guess > random_num:
            print('Lower')
        elif user_guess < random_num:
            print('Higher')
        else:
            print('Congratulations, you\'ve guessed the number!')
            sys.exit()
    
    except ValueError:
        print('Please enter a valid number')

    
    