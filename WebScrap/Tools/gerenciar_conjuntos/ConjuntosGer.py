from bs4 import BeautifulSoup
from Tools.coletar_infos import Infos
from Tools.salvar_json import SalvarJson
from concurrent.futures import ThreadPoolExecutor


salas_organizadas = []

def coletar_conjuntos_res(sala_res) -> list:
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

def organizar_conjunto(conjunto_res) -> list:
    '''
    Organiza o conjunto recebido transformando ele em um dicionario
    '''
    conjunto_nome = conjunto_res[0].text.strip()
    print(f'======{conjunto_nome}=========', 'iniciado')
    num_objetivo = int(len(conjunto_res[1].find_all(class_='center'))) - 1

    if 'ouros' in conjunto_nome:
        return [{conjunto_nome: conjunto_nome.replace('Conjunto ', '')}, num_objetivo]

    conjunto = [{conjunto_nome: []}, num_objetivo]

    items_nomes = []

    for info in conjunto_res[1:-1]:
        item_nome = info.text.strip().split('\n')[0]

        if item_nome not in items_nomes:
            items_nomes.append(item_nome)

    results = Infos.coletar_multiplas_infos(items_nomes)

    conjunto[0][conjunto_nome] = results

    print(f'======{conjunto_nome}=========', 'finalizado')

    return conjunto

def main(sala):
    conjuntos = []

    conjuntos_res = coletar_conjuntos_res(sala)

    for conjunto_res in conjuntos_res:
        conjunto = organizar_conjunto(conjunto_res)
        conjuntos.append(conjunto)

    salas_organizadas.append(conjuntos)

def multiples(salas):
    result = {}
    res_salas = []
    for n, nome in enumerate(salas):
        # res_salas.append(salas[nome])

        main(salas[nome])
        result[nome] = salas_organizadas[n]

    return result