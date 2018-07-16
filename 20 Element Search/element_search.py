# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
# largest) and another number. The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.
#
# Extras:
#
#     Use binary search.
import random


def busca_binaria_lista(lista, numero_usuario):
    primeiro = 0
    ultimo = len(lista) - 1
    encontrado = False

    while primeiro <= ultimo and not encontrado:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == numero_usuario:
            encontrado = True
        else:
            if numero_usuario < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return encontrado


def busca_in_lista(lista, numero_usuario):
    return True if numero_usuario in lista else False


a = [1, 3, 5, 30, 42, 43, 500]

print(busca_binaria_lista(a, 555))
