from bs4 import BeautifulSoup

class Conjuntos():
    def __init__(self, res, salas):
        self.res = res
        self.salas = salas
                    
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
        salas_organizadas = []
        
        for sala in self.salas[:6]:
            conjuntos = []
            conjuntos_res = self.coletar_conjuntos(sala)
            
            for conjunto_res in conjuntos_res:
                conjunto = self.organizar_conjunto(conjunto_res)
                
                conjuntos.append(conjunto)

            salas_organizadas.append(conjuntos)
        
        print(salas_organizadas)
        return salas_organizadas