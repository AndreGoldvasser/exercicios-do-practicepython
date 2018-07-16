# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the
#  user the same string, except with the words in backwards order. For example, say I type the string:
#
#   My name is Michele
#
# Then I would see the string:
#
#   Michele is name My
#
# shown back to me.

def reverte_ordem_string(string_frase="Ola Mundo"):
    print(" ".join(string_frase.split()[::-1]))


reverte_ordem_string(str(input("Escreva uma frase para inverter sua ordem.")))
