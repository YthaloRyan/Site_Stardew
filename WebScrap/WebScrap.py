import requests
from Tools.coletar_salas import Salas
from Tools.gerenciar_conjuntos import ConjuntosGer
from Tools.salvar_json import SalvarJson
import time


class Stardew:
    def __init__(self):
        self.base_url = 'https://pt.stardewvalleywiki.com/'
        self.res = requests.get(f'{self.base_url}Conjuntos').text

    def stardew_salas(self) -> dict:
        salas = {}
        scrap_salas = Salas.ScrapSalas(self.res)

        nomes_salas = scrap_salas.coletar_nomes_salas()
        res_salas = scrap_salas.coletar_salas()

        for n, nome in enumerate(nomes_salas):
            salas[nome] = res_salas[n]

        return salas

    def main(self):
        salas = self.stardew_salas()
        resultado = ConjuntosGer.multiples(salas)

        SalvarJson.salvar_json('dados', resultado)


if __name__ == "__main__":
    start_time = time.time()

    Stardew().main()
    end_time = time.time()

    elapsed_time = end_time - start_time
    print("Tempo decorrido:", elapsed_time, "segundos")
