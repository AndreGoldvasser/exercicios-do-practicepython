# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
# first and last elements of the given list. For practice, write this code inside a function.
import random

def first_last_list(lista):
    if len(lista) == 0:
        return []
    elif len(lista) == 1:
        return [lista[0]]
    else:
        return [lista[0], lista[-1]]

lista = random.sample(range(1,100), random.randrange(1,20))
print(lista)
print(first_last_list(lista))
