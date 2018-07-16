# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock
def fazer_jogada(jogada=''):
    while jogada not in possiveis_jogadas:
        jogada = str.lower(input("Pedra, Papel ou Tesoura?"))
    return jogada


def decisao(p1, p2):
    if p1['jogada'] == p2['jogada']:
        print("Empate técnico.")

    elif p1['jogada'] == 'pedra' and p2['jogada'] == 'tesoura':
        print(p1['nome'] + " vence.")
    elif p1['jogada'] == 'papel' and p2['jogada'] == 'pedra':
        print(p1['nome'] + " vence.")
    elif p1['jogada'] == 'tesoura' and p2['jogada'] == 'papel':
        print(p1['nome'] + " vence.")

    elif p1['jogada'] == 'tesoura' and p2['jogada'] == 'pedra':
        print(p2['nome'] + " vence.")
    elif p1['jogada'] == 'pedra' and p2['jogada'] == 'papel':
        print(p2['nome'] + " vence.")
    elif p1['jogada'] == 'papel' and p2['jogada'] == 'tesoura':
        print(p2['nome'] + " vence.")


rematch = True
player_1 = dict(nome='', jogada='')
player_2 = dict(nome='', jogada='')
possiveis_jogadas = ['pedra', 'papel', 'tesoura']

player_1['nome'] = input("Um nome para player_1")
player_2['nome'] = input("Um nome para player_2")
while rematch == True:
    player_1['jogada'] = fazer_jogada()
    player_2['jogada'] = fazer_jogada()
    decisao(player_1, player_2)

    if str.lower(input("Deseja começar um novo jogo? (sim) ou (não)")) == 'sim':
        rematch = True
    else:
        rematch = False
