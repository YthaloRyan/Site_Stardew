import json
import os

def salvar_json(nome, conteudo):
    
    # Caminho da pasta onde você quer salvar o JSON
    caminho_pasta = r"C:\Users\Produtivo\Desktop\Python\Site-Stardew\WebScrap\Arquivos"

    # Combinando o caminho da pasta e o nome do arquivo
    caminho_arquivo = os.path.join(caminho_pasta, f'{nome}.json')

    # Serializando o objeto JSON para uma string
    json_string = json.dumps(conteudo, ensure_ascii=False, indent=4)
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(json_string)