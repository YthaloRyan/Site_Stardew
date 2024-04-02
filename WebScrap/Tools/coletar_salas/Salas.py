from bs4 import BeautifulSoup

class ScrapSalas:
    def __init__(self, site_res):
        self.bs_salas = BeautifulSoup(site_res, 'html.parser')
    
    def coletar_salas(self):
        salas = []
        salas_res = self.bs_salas.find(class_='mw-content-ltr').find('div', class_='mw-parser-output').find_all('table')

        for sala in salas_res[1:]:
            if sala.find(class_='wikitable'):
                salas.append(sala)
           
        return salas
    
    def coletar_nomes_salas(self):
        nomes_salas = []
        nomes_salas_res = self.bs_salas.find_all('h2')
        
        for nome in nomes_salas_res[2:8]:
            nomes_salas.append(nome.text)
        
        return nomes_salas