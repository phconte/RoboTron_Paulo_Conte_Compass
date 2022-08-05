# Listar todos os dados de determinado elemento, buscando através do seu símbolo.

import pandas as pd

def func2():
    print('==' * 10)

    Tabela = pd.read_csv('Tabela.csv', encoding='UTF-8', sep=',')

    sb = str(input('Digite o simbolo do elemento desejado: '))

    if Tabela['Simbolo'].str.contains(sb).any():
        print(Tabela[Tabela['Simbolo'] == sb])
    else:
        print('Lista não contém elemento')


# Referência: lógica booleana e string dentro de um dataframe
# https://stackoverflow.com/questions/30944577/check-if-string-is-in-a-pandas-dataframe
