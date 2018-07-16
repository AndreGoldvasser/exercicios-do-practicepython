# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# Melhorar algoritmo para reduzir iterações

lista_divisores = []

numero = int(input("Digite um número: "))

for x in range(1, numero):
    if numero % x == 0:
        lista_divisores.append(x)

print(lista_divisores)
