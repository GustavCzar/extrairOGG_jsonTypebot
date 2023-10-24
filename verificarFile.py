import json

# Nome do arquivo JSON
nome_arquivo = 'MyLeads Vitanobis.json'

# Carregue o arquivo JSON
with open(nome_arquivo, 'r') as f:
    data = json.load(f)

# Imprima todas as chaves no JSON
for chave in data.keys():
    print(chave)
