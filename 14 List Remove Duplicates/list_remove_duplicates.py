# Write a program (function!) that takes a list and returns a new list that contains
#  all the elements of the first list minus all the duplicates.
#
# Extras:
#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
import random

def remove_duplicatas_lista(lista):
    lista_sem_duplicatas = []
    for x in lista:
        if x not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(x)
        else:
            pass
    return lista_sem_duplicatas

def remove_duplicatas_set(lista):
    lista_sem_duplicatas = set()
    for x in lista:
        lista_sem_duplicatas.add(x)
    return lista_sem_duplicatas

lista = random.sample(range(100),random.randint(8,19))
print(remove_duplicatas_lista(lista))
print(remove_duplicatas_set(lista))