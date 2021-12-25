import random

def create_random_numbers(size_of_array):
    numbers = []
    for i in range(size_of_array):
        numbers.append(random.randint(1,100000))
    return  numbers