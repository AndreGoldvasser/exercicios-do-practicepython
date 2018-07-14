# Use the BeautifulSoup and requests Python packages
# to print out a list of all the article titles
# on the New York Times homepage.
import requests
from bs4 import BeautifulSoup
url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
requisicao = requests.get(url)
pagina_bs = BeautifulSoup(requisicao.text,'html.parser')

for titulos in pagina_bs.find_all("p"):
    print(" ".join(titulos.text.split()))

