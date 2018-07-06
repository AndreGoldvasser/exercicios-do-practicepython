# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.



def is_even(num,divisor=2):
    if num % divisor == 0:
        return True
    return False

num = int(input("Digite um número: "))
print("Par") if is_even(num) else print("Ímpar")
divisor = int(input("Digite um divisor para o número anterior: "))
print("É divisível") if is_even(num,divisor) else print("Não é divisível")


