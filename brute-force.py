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

# get password input from user; verify that password only contains lowercase characters or digits
def get_password_input():
    password = input('Enter password to brute force: ')
    if not password.islower() and not password.isdigit():
        print('Password must only contain lowercase characters or digits.')
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

# calculate number of guesses based on password 
def calculate_guesses(password):
    chars = string.ascii_lowercase + string.digits
    total_guesses = 0

    for i in range(1, len(password)):
        total_guesses += len(chars) ** i

    for i in range(len(password)):
        total_guesses += chars.index(password[i]) * (len(chars) ** (len(password) - i - 1))

    return total_guesses + 1

# estimate time taken to brute force password
def estimate_time(password):
    total_guesses = calculate_guesses(password)
    time_per_guess = find_time_per_guess()
    time_taken = total_guesses * time_per_guess
    return time_taken

if __name__ == '__main__':
    password = get_password_input()
    print(f"A password of length {len(password)} could take {calculate_guesses(password)} guesses to guess.")
    print(guess_password(password))
