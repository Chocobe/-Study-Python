import random

def create_random_number():
    return random.randint(1, 45)

def generate_lotto_numbers():
    lotto_numbers = set()

    while len(lotto_numbers) < 5:
        lotto_numbers.add(create_random_number())

    return list(lotto_numbers)

print('generate_lotto_numbers(): ', generate_lotto_numbers())
