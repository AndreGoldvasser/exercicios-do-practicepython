# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
#
#     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#     Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

# Fazer um prompt pra quantas_mensagens repetir
# Simplificar o formatamento nos prints
from datetime import datetime

def calcula_aos_100(nome, idade):
    ano_atual = int(datetime.today().strftime("%Y"))
    quantas_mensagens = 5
    for x in range(quantas_mensagens):
        if idade < 100:
            print(nome + ", você vai fazer 100 anos em " + str(ano_atual + (100 - idade)))
        elif idade == 100:
            print("Estamos em " + str(ano_atual) + ", e " + nome + " tem 100 anos de vida.")
        else:
            print("Você está velho demais para executar esse programa.")

nome = input("Digite seu nome: ")
idade = int(input("Quantos anos você tem?"))
calcula_aos_100(nome, idade)


