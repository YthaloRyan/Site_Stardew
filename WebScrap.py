import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

def salvador(nome, conteudo):
    with open(nome, 'w') as arquivo_html:
        arquivo_html.write(str(conteudo))

def salvador_json(nome, conteudo):
    with open(f'{nome}.json', 'w', encoding='utf-8') as arquivo_json:
        json.dump(conteudo, arquivo_json, ensure_ascii=False, indent=4)
        
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
        
    def coletar_salas(self):
        salas = []
        salas_res = BeautifulSoup(self.res, 'html.parser').find(class_='mw-content-ltr').find('div', class_='mw-parser-output').find_all('table')
    
        for sala in salas_res[1:]:
            if sala.find(class_='wikitable'):
                salas.append(sala)
                
        return salas
                    
    def coletar_conjuntos(self, sala_res):
        conjuntos = []

        conjuntos_res = sala_res.find_all('table', class_='wikitable')
        
        for conjunto_res in conjuntos_res:
            if conjunto_res.get('style'):
                continue
            
            nomes = conjunto_res.find_all('tr')
            conjuntos.append(nomes)
        
        return conjuntos
    
    def organizar_conjunto(self, conjunto_res):
        titulo = conjunto_res[0].text.strip()
        conjunto = [titulo]
        
        for info in conjunto_res[1:-1]:
            item = info.text.strip().split('\n')[0]
            
            if item not in conjunto:
                conjunto.append(item)
        
        return conjunto
            
    def main(self):
        self.teste = False
        salas_organizada = []
        salas = self.coletar_salas()
        
        for sala in salas[:6]:
            conjuntos = []
            conjuntos_res = self.coletar_conjuntos(sala)
            
            for conjunto_res in conjuntos_res:
                conjunto = self.organizar_conjunto(conjunto_res)
                
                conjuntos.append(conjunto)
                
                
            
            
            salas_organizada.append(conjuntos)
            
            
        
        
        salvador_json('salvapf', salas_organizada)

if __name__ == "__main__":
    Stardew().main()