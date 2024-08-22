import json
import pandas as pd


with open('./WebScrap\Arquivos\dados.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for sala in data:
    df = pd.DataFrame(data[sala])

    # Caminho para salvar o arquivo Excel
    excel_file_path = './dados.xlsx'

    # Salvar o DataFrame em um arquivo Excel
    df.to_excel('./dados.xlsx', index=False)

    print(f'Dados salvos em {excel_file_path}')
    
    exit()
