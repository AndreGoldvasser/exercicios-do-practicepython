# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


def is_even(num, divisor=2):
    try:
        if num % divisor == 0:
            return True
        return False
    except ZeroDivisionError:
        print("DIVISÃO POR ZERO. AÍ NÃO NÉ PARSSA. ERROR.")


num = int(input("Digite um número: "))
if num % 4 == 0:
    print("Divisor de 4(multiple of 4, print out a different message).")
else:
    print("Par") if is_even(num) else print("Ímpar")
divisor = int(input("Digite um divisor para o número anterior: "))
print("É divisível") if is_even(num, divisor) else print("Não é divisível")
