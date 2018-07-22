# In this exercise, the task is to write a function that picks a random word from a list of words from the
# SOWPODS dictionary. Download this file and save it in the same directory as your Python code. This file
# is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each
# line in the file contains a single word.
#
# Hint: use the Python random library for picking a random word.
import random


def main():
    print(f'Aqui vai: {random_line_pick().lower().title()}')


def random_line_pick():
    with open('reset.txt', 'r') as open_file:
        random_line = random.choice(open_file.read().splitlines())
    return random_line


if __name__ == '__main__':
    main()
