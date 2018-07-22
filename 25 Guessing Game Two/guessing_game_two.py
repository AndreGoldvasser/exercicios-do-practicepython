# The user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user,
#  will say whether it is too high, too low, or your number.
# At the end of this exchange, your program should print out how many guesses it took to get your number.
# As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy
#  can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not
#   an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and
#    then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy!
#    (We’ll talk about what is the optimal one next week with the solution.)

import random


def main():
    guess_game()


def introducao(menor, maior):
    print(f'...Pense em um número entre {menor} e {maior}')
    print('Responda de acordo a seguir...')
    input("Digite enter para continuar.")


def guess_game():
    guess_COM = random.randint(40, 60)
    found = False
    menor = 0
    maior = 100
    numero_tentativa = 0
    introducao(menor, maior)
    while not found:
        print(f'guess_COM adivinhou: {guess_COM}')
        print('O número que tu pensas é: maior, menor ou correto?\n')
        resposta = input().lower()
        if resposta == 'maior':
            menor = guess_COM
        elif resposta == 'menor':
            maior = guess_COM
        elif resposta == 'correto':
            found = True
        else:
            print("Digite um dos 3 para continuar.")
        guess_COM = (maior + menor) // 2
        numero_tentativa += 1
    print(f'O número foi adivinhado com êxito após {numero_tentativa} ', end='')
    print('vezes.' if numero_tentativa != 1 else 'vez.')


if __name__ == '__main__':
    main()
