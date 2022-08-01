# Do JSON 1 Guarde apenas o Nome do Estádio, o Placar e o Status 
# do jogo dentro de variáveis e mostre-as

import json


def retornar_json():
    with open("JSON1.json", encoding="utf-8") as partida:
        json_manipulavel = json.load(partida)
        return json_manipulavel


json_retornado = retornar_json()

campeonato = json_retornado['copa-do-brasil'][0]
estadio = campeonato['estadio']

placar_mandante = campeonato["placar_mandante"]
placar_visitante = campeonato["placar_visitante"]
nome_estadio = estadio["nome_popular"]
status = campeonato["status"]

print('O jogo no estádio', nome_estadio, 'está', status, 'e o resultado foi Sto André', placar_mandante, 'x', placar_visitante, 'Criciúma')


# Referências:
# Video 02 da aula do dia 06 da sprint 04: LEITURA-JSON-SIMPLES-COM-PYTHON-EDITADO
# Correção do erro 'TypeError list indices must be integers not str' https://stackoverflow.com/questions/24708634/python-and-json-typeerror-list-indices-must-be-integers-not-str
