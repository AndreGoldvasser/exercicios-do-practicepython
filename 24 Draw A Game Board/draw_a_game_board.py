def main():
    try:
        size = int(input('Digite o número de quadrados:\n'))
    except ValueError:
        print('Erro de input. Insira um valor int.')
        exit(-1)
    game = [[0 for elemento_a in range(size)] for elemento_b in range(size)]
    draw_board(game)


def draw_board(game):
    for piece in range(len(game)):
        for element in range(len(game)):
            print(' ---', end='')
        print()
        for element in range(len(game)):
            if game[piece][element] == 0:
                print('|   |', end='') if element == len(game) - 1 else print('|   ', end='')
            else:
                print('| ', end='')
                print('X ', end='') if game[piece][element] == 1 else print('O ', end='')
                if element == len(game) - 1:
                    print('|', end='')
        print()
    for element in range(len(game)):
        print(' ---', end='')
    print()


if __name__ == '__main__':
    main()
