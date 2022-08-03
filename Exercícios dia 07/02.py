# Pegue o arquivo JSON 1 e printe apenas o nome do time vencedor no terminal

import json


def retornar_json():
    with open("JSON1.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel


partida = retornar_json()

campeonato = partida['copa-do-brasil'][0]
mandante = campeonato['time_mandante']
visitante = campeonato['time_visitante']

placar_mandante = campeonato["placar_mandante"]
placar_visitante = campeonato["placar_visitante"]
time_mandante = mandante["nome_popular"]
time_visitante = visitante["nome_popular"]

if placar_mandante > placar_visitante:
    print("O vencedor foi o:", time_mandante)
else:
    print("O vencedor foi o:", time_visitante)

# Referências:
# Video 02 da aula do dia 06 da sprint 04: LEITURA-JSON-SIMPLES-COM-PYTHON-EDITADO
# Correção do erro 'TypeError list indices must be integers not str' https://stackoverflow.com/questions/24708634/python-and-json-typeerror-list-indices-must-be-integers-not-str
