import os
import sys
from pathlib import Path

sys.path.insert(1, str(Path(__file__).parents[1]) + '/26 Check Tic tac Toe')
sys.path.insert(1, str(Path(__file__).parents[1]) + '/24 Draw A Game Board')
import draw_a_game_board




def main():
    game = [[0 for elemento_a in range(3)] for elemento_b in range(3)]
    while 0 in game:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_a_game_board.draw_board(game)
        input_player('one')
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_a_game_board.draw_board(game)
        input_player('two')


def input_player(player_number):
    jogada = input(f'Player {player_number},'
                   f'\npor favor digite a linha e coluna,'
                   f'\nseparados por uma vírgula para inserir a jogada.')
    jogada = jogada.split(',')
    jogada = [int(x) - 1 for x in jogada]
    if game[jogada[0]][jogada[1]] is 0:
        if player_number == 'one':
            game[jogada[0]][jogada[1]] = 1
        else:
            game[jogada[0]][jogada[1]] = 2
    else:
        print("Espaço já ocupado, tente novamente.")
        input_player(player_number)


if __name__ == '__main__':
    main()
