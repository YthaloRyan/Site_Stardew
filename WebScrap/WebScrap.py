import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from Tools.coletar_salas import Salas
from Tools.gerenciar_conjuntos import ConjuntosGer
from Tools.salvar_json import SalvarJson


      
class Stardew:
    def __init__(self):
        self.base_url = 'https://pt.stardewvalleywiki.com/'
        
    def main(self):
        resultado = {}
        self.res = requests.get(f'{self.base_url}Conjuntos').text
        scrap_salas = Salas.ScrapSalas(self.res)
        
        nomes_salas = scrap_salas.coletar_nomes_salas()
        salas = scrap_salas.coletar_salas()
        
        scrap_conjuntos = ConjuntosGer.Conjuntos(self.res, salas)
        
        conjuntos = scrap_conjuntos.main()
        
        for n, nome in enumerate(nomes_salas):
            resultado[nome] = conjuntos[n]
         
        SalvarJson.salvar_json('dados', resultado)
        
        

if __name__ == "__main__":
    Stardew().main()