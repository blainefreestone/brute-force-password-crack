import itertools
import string
import time

# brute forces a password of lowercase alphanumeric characters
def guess_password(password):
    # used to calculate time taken to find password
    start = time.time()

    # characters that can be used in password
    chars = string.ascii_lowercase  + string.digits
    attempts = 0

    # recursively generate all possible passwords of length 1-8
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                end = time.time()
                distance = end - start
                return (f'\rPassword is {guess}. Found in {attempts} guesses and {distance} seconds.')
            print('\r' + guess, end='')
    return 'Password not in the list'

# get password input from user and verify that it is lowercase alphanumeric
def get_password_input():
    password = input('Enter password to brute force: ')
    if not password.islower():
        print('Password must be lowercase alphanumeric characters.')
        return get_password_input()
    return password
