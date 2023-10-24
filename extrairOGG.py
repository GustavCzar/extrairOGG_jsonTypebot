import json
import base64

# Nome do arquivo JSON
nome_arquivo = 'MyLeads Vitanobis.json'

# Aqui você carrega o arquivo JSON
with open(nome_arquivo, 'r') as f:
    data = json.load(f)

# Acessar a lista associada à chave 'backup'
backup = data['backup']

# Percorrer cada item na lista 'backup'
for i, item in enumerate(backup):
    # O áudio está sob a chave 'file'
    audio_base64 = item['file']

    # O audio_base64 contém um prefixo que precisamos remover antes de decodificar
    prefixo, audio_base64 = audio_base64.split(',')

    # Decodifique o áudio base64 para bytes
    audio_bytes = base64.b64decode(audio_base64)

    # Escreva os bytes em um arquivo OGG
    with open(f'saida{i}.ogg', 'wb') as f:
        f.write(audio_bytes)
