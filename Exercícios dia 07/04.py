# No JSON 1 printe todas as chaves e valores do time visitante

import json


def retornar_json():
    with open("JSON1.json", encoding="utf-8") as partida:
        json_manipulavel = json.load(partida)
        return json_manipulavel


json_retornado = retornar_json()

campeonato = json_retornado['copa-do-brasil'][0]
visitante = campeonato['time_visitante']

time_visitante_id = visitante["time_id"]
time_visitante = visitante["nome_popular"]
time_visitante_sigla = visitante["sigla"]
time_visitante_escudo = visitante["escudo"]

print('O time visitante é o', time_visitante, 'de ID',time_visitante_id,'sigla', time_visitante_sigla, 'e possui o escudo', time_visitante_escudo)