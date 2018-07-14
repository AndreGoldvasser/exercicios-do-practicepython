# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
# largest) and another number. The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.
#
# Extras:
#
#     Use binary search.
import random

# def binary_search_list(lista,numero_usuario):
#     meio_da_lista = int(len(lista)/2)
#     if numero_usuario == lista[meio_da_lista]:
#         return True
#     elif numero_usuario < lista[meio_da_lista]:
#         binary_search_list(lista[:int(len(lista)/2)],numero_usuario)
#     else:
#         binary_search_list(lista[int(len(lista)/2):],numero_usuario)
def binary_search

def search_list(lista,numero_usuario):
    return True if numero_usuario in lista else False



a = [1, 3, 5, 30, 42, 43, 500]
# print(int(len(a)/2))

print(binary_search_list(a,500))
