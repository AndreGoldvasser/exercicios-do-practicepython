# Take two lists, and write a program that returns a list that contains only the elements that are common
#  between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
#
# Extras:
#     Randomly generate two lists to test this
#     Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

if __name__ == '__main__':
    a = random.sample(range(100), random.randint(8, 19))
    b = random.sample(range(100), random.randint(7, 21))
    print([numero for numero in a if numero in b])
