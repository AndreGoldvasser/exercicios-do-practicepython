# Given a .txt file that has a list of a bunch of names, count how many of each name there
# are in the file, and print out the results to the screen. I have a .txt file for you, if
# you want to use it!
#
# Extra:
#
#     Instead of using the .txt file from above (or instead of, if you want the challenge),
#  take this .txt file, and count how many of each “category” of each image there are.
#  This text file is actually a list of files corresponding to the SUN database scene
#  recognition database, and lists the file directory hierarchy for the images. Once you
#  take a look at the first line or two of the file, it will be clear which part
#  represents the scene category. To do this, you’re going to have to remember a bit
#  about string parsing in Python 3. I talked a little bit about it in this post.
def main():
    conta_categoria()
    conta_nomes("nameslist")


def print_dict(dict):
    for key, value in dict.items():
        print(f'{key} : {value} vezes')


def conta_nomes(file_name):
    dict_nomes = {}
    with open(file_name + '.txt', 'r') as open_file:
        texto = open_file.read().split()
    for linha in texto:
        if linha in dict_nomes.keys():
            dict_nomes[linha] += 1
        else:
            dict_nomes[linha] = 1
    print_dict(dict_nomes)


def conta_categoria():
    dict_categorias = {}
    with open('training_01.txt', 'r') as open_file:
        texto = open_file.read().split()
        # print(texto[2])
    for linha in texto:
        linha = linha.split('/')

        if linha[2] in dict_categorias.keys():
            dict_categorias[linha[2]] += 1
        else:
            dict_categorias[linha[2]] = 1
    print_dict(dict_categorias)


if __name__ == '__main__': main()
