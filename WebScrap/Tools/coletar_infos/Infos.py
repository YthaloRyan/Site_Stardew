import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor

class Coletar:
    def __init__(self, item_nome):
        self.url_base = 'https://pt.stardewvalleywiki.com/'
        self.item_nome = item_nome
        self.infos_dict = {self.item_nome: {}}
        self.titulos = ['Local(is)', 'Hora', 'Estação', 'Tempo', 'Origem']
        self.url = self.url_base + self.item_nome.split('(')[0].strip()

    def coletar_res(self):
        try:
            res = requests.get(self.url)
            self.soup = BeautifulSoup(res.text, 'html.parser')
        except:
            print(f'Erro {res} - {self.item_nome}')

    def coletar_infos(self):
        trs = self.soup.find('table').find_all('tr')
        for tr in trs:
            try:
                titulo = tr.find('td', id='infoboxsection').text.strip()
            except:
                continue
            
            
            if titulo in self.titulos:
                infos = []
                infobox = tr.find(id='infoboxdetail')
                infos_res = infobox.find_all('span')
        
                if infos_res:
                    for info in infos_res:
                        info = info.text.strip()
                        
                        
                        if ' • ' not in info:
                            infos.append(info)
                
                else:
                    info = infobox.text.strip()
                    
                    
                    if titulo == 'Hora':
                        infos = ' - '.join(info.split(' ')[::2])
                        
                    else:   
                        infos = info.split(' • ')

                if len(infos) == 1:
                    infos = ''.join(infos)
                
                self.infos_dict[self.item_nome][titulo] = infos

    def start(self) -> dict:
        print(self.item_nome, 'iniciado')

        self.coletar_res()
        self.coletar_infos()

        print(self.item_nome, 'finalizado')

        return self.infos_dict

def coletar_infos(item_nome):
    return Coletar(item_nome).start()

def coletar_multiplas_infos(items_nomes: list) -> list:
    finalizado = []

    with ThreadPoolExecutor(max_workers=len(items_nomes)) as executor:
        resultados_futuros = [executor.submit(coletar_infos, item) for item in items_nomes]

    for resultado in resultados_futuros:
        finalizado.append(resultado.result())

    return finalizado

