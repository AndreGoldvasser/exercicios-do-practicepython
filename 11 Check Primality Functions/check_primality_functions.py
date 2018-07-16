# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
# a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.
def is_prime(number):
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    else:
        prime = True
        for check_number in range(2, int((number / 2) + 1)):
            if number % check_number == 0:
                prime = False
                break
    return prime


number = int(input("Digite um número:\n"))
print(number, "é um número primo") if is_prime(number) else print(number, "não é um número primo.")
