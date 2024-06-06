# import random

# def create_random_number():
#     return random.randint(1, 45)

# def generate_lotto_numbers():
#     lotto_numbers = []

#     while len(lotto_numbers) < 6:
#         random_number = create_random_number()

#         if random_number not in lotto_numbers:
#             lotto_numbers.append(random_number)

#     return lotto_numbers

# print('generate_lotto_number(): ', generate_lotto_numbers())

#
# ---
#

import random

def generate_random_number():
    return random.randint(1, 45)

def generate_lotto_numbers():
    lotto_numbers = []

    while len(lotto_numbers) < 6:
        random_number = generate_random_number()

        if random_number not in lotto_numbers:
            lotto_numbers.append(random_number)

    return lotto_numbers

print('generate_lotto_numbers(): ', generate_lotto_numbers())
