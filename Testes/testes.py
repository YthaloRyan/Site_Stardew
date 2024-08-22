import requests
from bs4 import BeautifulSoup

res = requests.get("https://pt.stardewvalleywiki.com/Conjuntos")

nomes_conjuntos = BeautifulSoup(res.text, 'html.parser').find_all('h2')

teste = BeautifulSoup(res.text, 'html.parser').find(class_='mw-content-ltr').find('div', class_='mw-parser-output').find_all('table')

conjuntos = teste.find_all('table')

for conjunto in conjuntos[1:]:
    if conjunto.find(class_='wikitable'):
        itens_conjuntos = conjunto.find_all(class_='wikitable')
        
        for itens in itens_conjuntos[1:]:
            print(itens)
            input()

exit()

for nome in nomes_conjuntos[2:8]:
    print(nome.text)

