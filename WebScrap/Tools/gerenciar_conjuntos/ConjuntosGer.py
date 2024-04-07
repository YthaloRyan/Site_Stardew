from bs4 import BeautifulSoup
from Tools.coletar_infos import infos

class Conjuntos():
    def __init__(self, res, salas):
        self.res = res
        self.salas = salas
                    
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
        num_objetivo = int(len(conjunto_res[1].find_all(class_='center'))) - 1
        
        conjunto = [{conjunto_nome: []}, num_objetivo]
        
        items_nomes = []
        for info in conjunto_res[1:-1]:
            item_nome = info.text.strip().split('\n')[0]
            
            if item_nome not in items_nomes:
                items_nomes.append(item_nome)
            
            if 'ouros' not in conjunto_nome:
                item = infos.itens().main(item_nome)
            else:
                item = item_nome
            
            if item not in conjunto[0][conjunto_nome]:
                conjunto[0][conjunto_nome].append(item)
        
        return conjunto
            
    def main(self) -> list:
        salas_organizadas = []
        
        for sala in self.salas[:6]:
            conjuntos = []
            conjuntos_res = self.coletar_conjuntos(sala)
            
            for conjunto_res in conjuntos_res:
                conjunto = self.organizar_conjunto(conjunto_res)
                
                conjuntos.append(conjunto)

            salas_organizadas.append(conjuntos)
        

        return salas_organizadas