import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor

class Coletar:
    def __init__(self):
        self.url_base = 'https://pt.stardewvalleywiki.com/'
    
    def coletar_res(self):
        url = f'{self.url_base}{self.item_nome.split('(')[0].strip()}'
                                                            
        try:
            res = requests.get(url)
        except:
            print(f'Erro {res} - {self.item_nome}')
        
        soup = BeautifulSoup(res.text, 'html.parser')
        
        return soup
    
    def coletar_infos(self):
        titulos = ['Local(is)', 'Hora', 'Estação', 'Tempo', 'Origem']
        
        trs = self.soup.find('table').find_all('tr')
        for tr in trs:
            try:
                titulo = tr.find('td', id='infoboxsection').text.strip()
            except:
                continue
             
            if titulo in titulos:
                infos = tr.find(id='infoboxdetail').text.strip()    
                self.infos_dict[self.item_nome][titulo] = infos
                
    def start(self, item_nome) -> dict:
        self.item_nome = item_nome
        print(self.item_nome, 'iniciado')
        self.infos_dict = {self.item_nome: {}}
        
        self.soup = self.coletar_res()
        
        self.coletar_infos()
        print(self.item_nome, 'finalizado')
        
        return self.infos_dict
        
def coletar_infos(item_nome):
    return Coletar().start(item_nome)      
        
def coletar_multiplas(items_nomes):
    finalizado = []
    
    with ThreadPoolExecutor(max_workers=len(items_nomes)) as executor:
        resultados_futuros = [executor.submit(coletar_infos, item) for item in items_nomes]
        
    for resultado in resultados_futuros:
        finalizado.append(resultado.result())
    
    return finalizado