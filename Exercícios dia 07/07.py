# Percorra o JSON 2, utilizando o loop FOR e printe suas chaves principais.

import json


def retornar_json():
    with open("JSON2.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel


campeonato = retornar_json()

for key in campeonato:
    print(key, ":", campeonato[key])


# Referência:
# Usar json.load() com ajuda de 'for' para ler um JSON
# https://www.delftstack.com/pt/howto/python/iterate-through-json-python/
