# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether
# anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a
# column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board
# there will only be one winner.
def main():
    game = [[2, 0, 1],
            [2, 2, 1],
            [1, 1, 2]]
    check_tic_tac_toe(game)


def check_tic_tac_toe(game):
    def check_line():
        for line in range(len(game)):
            if game[line][0] == game[line][1] and game[line][0] == game[line][2]:
                if game[line][0] != 0:
                    declare_winner(game[line][0])

    def check_column():
        for coluna in range(len(game)):
            if game[0][coluna] == game[1][coluna] and game[0][coluna] == game[2][coluna] and not 0:
                # if game[0][coluna] != 0:
                declare_winner(game[0][coluna])

    def check_diagonal():
        if game[0][0] == game[1][1] and game[0][0] == game[2][2]:
            if game[0][0] != 0:
                declare_winner(game[0][0])
        if game[0][2] == game[1][1] and game[0][2] == game[2][0]:
            if game[0][0] != 0:
                declare_winner(game[0][2])

    def declare_winner(player):
        if player == 1:
            print("Player 1 venceu.")
        if player == 2:
            print("Player 2 venceu.")
        print('FDSFDSFDS\n \n \n \n')


    check_line()
    check_column()
    check_diagonal()


if __name__ == '__main__':
    main()
