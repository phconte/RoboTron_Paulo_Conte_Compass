# Faça com que o programa printe apenas os primeiros dados
# dentro de edicao_atual, fase_atual, rodada_atual usando o JSON 2.

import json


def retornar_json():
    with open("JSON2.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel


campeonato = retornar_json()

edicao_atual = campeonato['edicao_atual']['edicao_id']
fase_atual = campeonato['fase_atual']['fase_id']
rodada_atual = campeonato['rodada_atual']['nome']
print('O Campeonato Brasileiro 2021 tem o ID', edicao_atual,
      'a atual fase tem o ID', fase_atual, 'e está na', rodada_atual)
