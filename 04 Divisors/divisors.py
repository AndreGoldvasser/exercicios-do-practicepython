# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
def main():
    numero_usuario = int(input("Digite um número: "))
    print(listar_divisores(numero_usuario))


def listar_divisores(numero_usuario):
    return [elemento for elemento in range(1, numero_usuario) if numero_usuario % elemento == 0]


if __name__ == '__main__': main()
