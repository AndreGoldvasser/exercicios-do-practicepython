# Use the BeautifulSoup and requests Python packages
# to print out a list of all the article titles
# on the New York Times homepage.
import requests
from bs4 import BeautifulSoup


def pega_paragrafos_html(url):
    requisicao = requests.get(url)
    pagina_bs = BeautifulSoup(requisicao.text, 'html.parser')
    for titulos in pagina_bs.find_all("h2", class_="story-heading"):
        print(" ".join(titulos.text.split()))


if __name__ == '__main__':
    pega_paragrafos_html('http://www.nytimes.com/')
