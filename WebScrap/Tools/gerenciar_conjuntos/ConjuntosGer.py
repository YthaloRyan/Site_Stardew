from bs4 import BeautifulSoup
from Tools.coletar_infos import infos
from concurrent.futures import ThreadPoolExecutor

class Conjuntos():
    def __init__(self, res, salas):
        self.res = res
        self.salas = salas
        self.url = 'https://pt.stardewvalleywiki.com/'
                    
    def coletar_conjuntos(self, sala_res) -> list:
        '''
        Coleta os conjuntos da sala_res recebida
        '''
        conjuntos = []

        conjuntos_res = sala_res.find_all('table', class_='wikitable')
        
        for conjunto_res in conjuntos_res:
            if conjunto_res.get('style'):
                continue
            
            nomes = conjunto_res.find_all('tr')
            conjuntos.append(nomes)
        
        return conjuntos
    
    def organizar_conjunto(self, conjunto_res) -> list:
        '''
        Organiza o conjunto recebido transformando ele em um dicionario
        '''
        conjunto_nome = conjunto_res[0].text.strip()
        print(f'======{conjunto_nome}=========', 'iniciado')
        num_objetivo = int(len(conjunto_res[1].find_all(class_='center'))) - 1
        
        if conjunto_nome == 'Cofre':
            return [{conjunto_nome: []}, num_objetivo]
        
        conjunto = [{conjunto_nome: []}, num_objetivo]
        
        items_nomes = []
        urls = []
        for info in conjunto_res[1:-1]:
            item_nome = info.text.strip().split('\n')[0]
            
            if item_nome not in items_nomes:
                items_nomes.append(item_nome)
                urls.append(f'{self.url}{item_nome.split('(')[0].strip()}')
        
        with ThreadPoolExecutor(max_workers=len(items_nomes)) as executor:
            results = list(executor.map(infos.main_teste, urls))
        
        # results = []
        # for url in urls:
        #     results.append(infos.main_teste(url))
        
        conjunto[0][conjunto_nome] = results
        
        print(f'======{conjunto_nome}=========', 'finalizado')
        return conjunto
            
    def main(self) -> list:
        salas_organizadas = []
        
        for sala in self.salas[:5]:
            conjuntos = []
            conjuntos_res = self.coletar_conjuntos(sala)
            
            for conjunto_res in conjuntos_res:
                conjunto = self.organizar_conjunto(conjunto_res)
                
                conjuntos.append(conjunto)

            salas_organizadas.append(conjuntos)
        

        return salas_organizadas