# Baixe o arquivo do link JSON 1, abra ele no vsCode com Python
# nomeando-o como "partida", guarde em uma variável e printe o JSON inteiro no terminal

import json


def retornar_json():
    with open("JSON1.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel


partida = retornar_json()
print(partida)

# Referência: video 02 da aula do dia 06 da sprint 04: LEITURA-JSON-SIMPLES-COM-PYTHON-EDITADO
