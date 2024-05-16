# a function that brute forces a password of alphanumeric characters
def get_password(password):
    import itertools
    import string
    import time
    start = time.time()
    chars = string.ascii_lowercase  + string.digits
    attempts = 0
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

# Test
print(get_password('123'))
print(get_password('1234'))
print(get_password('blai'))
print(get_password('ste'))