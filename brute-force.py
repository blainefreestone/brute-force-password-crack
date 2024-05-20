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

# find time taken to make individual guesses
def find_time_per_guess():
    chars = string.ascii_lowercase + string.digits
    start = time.time()
    for char in chars:
        guess = char
    end = time.time()
    return end - start

# calculate number of guesses based on password length
def calculate_guesses(password):
    chars = string.ascii_lowercase + string.digits

    total_guesses = len(chars) ** len(password)

    return total_guesses

# estimate time taken to brute force password
def estimate_time(password):
    total_guesses = calculate_guesses(password)
    time_per_guess = find_time_per_guess()
    time_taken = total_guesses * time_per_guess
    return time_taken

if __name__ == '__main__':
    password = get_password_input()
    print(f"A password of length {len(password)} could take {estimate_time(password)} seconds to guess.")
    print(guess_password(password))
