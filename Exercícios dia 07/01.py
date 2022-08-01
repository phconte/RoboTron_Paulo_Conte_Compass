# Baixe o arquivo do link JSON 1, abra ele no vsCode com Python 
# nomeando-o como "partida", guarde em uma variável e printe o JSON inteiro no terminal

import json

def retornar_json():
    with open ("JSON1.json", encoding="utf-8") as partida:
        json_manipulavel = json.load(partida)
        return json_manipulavel

json_retornado = retornar_json()
print(json_retornado)

# Referência: video 02 da aula do dia 06 da sprint 04: LEITURA-JSON-SIMPLES-COM-PYTHON-EDITADO