import json
import os

def salvar_json(nome, conteudo):
    caminho_pasta = r"C:\Users\Produtivo\Desktop\Python\Site-Stardew\WebScrap\Arquivos"

    caminho_arquivo = os.path.join(caminho_pasta, f'{nome}.json')

    json_string = json.dumps(conteudo, ensure_ascii=False, indent=4)
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(json_string)

    print('Json Salvo')