# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether
# they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random

guesses_total = 0
guess = 0
while guess != 'exit':
    random_number = random.randint(1, 9)
    while int(guess) > 0 and int(guess) <= 9 or guess != 'exit':
        guess = str(input("Adivinhe um número entre 1 e 9, ou digite exit para sair do programa.\n"))
        if guess == 'exit':
            break
        elif int(guess) < random_number:
            print("Valor abaixo.")
        elif int(guess) == random_number:
            print("Na mosca.")
            random_number = random.randint(1, 9)
        elif int(guess) > random_number:
            print("Valor acima.")
        guesses_total += 1
    print("Número de tentativas: " + str(guesses_total))