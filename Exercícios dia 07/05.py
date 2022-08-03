# Guarde o arquivo JSON 2 nomeando-o como campeonato
# em uma variável e printe todos os seus dados.

import json


def retornar_json():
    with open("JSON2.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel


campeonato = retornar_json()
print(campeonato)

# Referência: video 02 da aula do dia 06 da sprint 04: LEITURA-JSON-SIMPLES-COM-PYTHON-EDITADO
