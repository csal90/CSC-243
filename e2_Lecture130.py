# guess(n) that simulates a number guesing game. It first generates a random numer
# between 1 and (n), then repeatedly prompts the user to enter the number guessed by the
# user, until the user enters the correct number.
# If the number entered by the user is larger than the randomly generated number
# It displays 'The number is too big'. If the number entered by the use is smaller
# Then the randomly generated number, it displayed 'The number is too small'.

# guess(10)
# it randomly generated a number 7
# Enter your guess: 5
# The number is too small


import random
def guess(n):
    while True:
        n=random.randint(1, n)
        i=int(input('Enter your guess: '))
        if i < n:
            print('Your number is too small')
        elif i > n:
            print('Your number is too large')
        elif i == n:
            break
        
    
