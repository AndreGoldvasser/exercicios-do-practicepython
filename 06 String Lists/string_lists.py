# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
def is_palindrome(user_string):
    return True if user_string == user_string[::-1] else False

user_string = str(input("Digite uma string :"))
print("É um palíndromo.") if is_palindrome(user_string) else print("Não é um palíndromo.")