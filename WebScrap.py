import requests
from bs4 import BeautifulSoup
from pprint import pprint

def salvador(nome, conteudo):
    with open(nome, 'w') as arquivo_html:
        arquivo_html.write(str(conteudo))
        
class Stardew:
    def __init__(self):
        self.base_url = 'https://pt.stardewvalleywiki.com/'
        
    def coletar_nomes_salas(self):
        nomes_salas = []
        nomes_salas_res = BeautifulSoup(self.res, 'html.parser').find_all('h2')
        
        for nome in nomes_salas_res[2:8]:
            nomes_salas.append(nome.text)
            
        return nomes_salas
        
    def main(self):
        self.res = requests.get(f'{self.base_url}Conjuntos').text
        infos = {}
        nomes_salas = self.coletar_nomes_salas()
        
        # print(nomes_salas)
        
        Conjuntos(self.res).main()
        
        
class Conjuntos():
    def __init__(self, res):
        self.res = res
        
    def coletar_conjuntos(self):
        conjuntos_res = BeautifulSoup(self.res, 'html.parser').find(class_='mw-content-ltr').find('div', class_='mw-parser-output').find_all('table')
        
        for conjunto in conjuntos_res[1:]:
            if conjunto.find(class_='wikitable'):
                itens_conjuntos = conjunto.find_all('td')
            
                self.filtrar_itens(itens_conjuntos)
                    
                    
    
    def filtrar_itens(self, conjuntos_res):
        
        for conjunto_res in conjuntos_res:
            salvador('teste', conjunto_res)
            
            input()
        
        
        input()
        
        # itens = itens_res.find_all(class_='wikitable')
        
        # print(itens_res)
        # print(itens)
        
        # for item in itens:
        #     print('Estouaqui')
        #     print(item.text)
        #     input()
            
    def main(self):
        conjuntos = self.coletar_conjuntos()

if __name__ == "__main__":
    Stardew().main()