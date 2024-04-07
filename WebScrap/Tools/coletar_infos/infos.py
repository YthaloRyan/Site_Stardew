import requests
from bs4 import BeautifulSoup

class itens:
    def main(self, item_name) -> dict:
        infos_dict = {item_name: {}}
        
        print(item_name, 'iniciado')
        titulos = ['Local(is)', 'Hora', 'Estação', 'Tempo', 'Origem']
        try:
            res = requests.get(f'https://pt.stardewvalleywiki.com/{item_name.split('(')[0].strip()}')
        except:
            print(item_name)
        
        soup = BeautifulSoup(res.text, 'html.parser')
        
        try:
            trs = soup.find('table').find_all('tr')
        except:
            print(item_name)
        
        for tr in trs:
            try:
                titulo = tr.find(id='infoboxsection').text
            except:
                continue
            
            if titulo in titulos:
                infos = tr.find(id='infoboxdetail').text 
                
                infos_dict[item_name][titulo] = infos    
        
        print(item_name, 'finalizado')
        return infos_dict