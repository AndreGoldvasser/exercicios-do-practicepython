# Take the code from the How To Decode A Website exercise (if you didn’t do it or just
# want to play with some different code, use the code from the solution), and instead
# of printing the results to a screen, write the results to a txt file. In your code,
# just make up a name for the file you are saving to.
#
# Extras:
#
#     Ask the user to specify the name of the output file that will be saved.

import requests
import codecs
from bs4 import BeautifulSoup


def pega_paragrafos_html(url):
    requisicao = requests.get(url)
    pagina_bs = BeautifulSoup(requisicao.text, 'html.parser')
    resultado = ''
    for titulos in pagina_bs.find_all("h2", class_="story-heading"):
        resultado += (" ".join(titulos.text.split()) + "\n")
    return resultado


def salva_texto(string):
    nome_do_arquivo = input("Digite um nome para o arquivo: \n")
    with codecs.open(nome_do_arquivo + ".txt", 'w', encoding='utf8') as open_file:
        open_file.write(string)


salva_texto(pega_paragrafos_html('http://www.nytimes.com/'))

pega_paragrafos_html('http://www.nytimes.com/')
