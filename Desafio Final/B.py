# Listar todos os dados de determinado elemento, buscando através do seu símbolo.

import pandas as pd


def func2():
    print('==' * 50)
    print(' ')

    Tabela = pd.read_csv('Tabela.csv', encoding='UTF-8', sep=',')

    sb = str(input(
        '    Digite o simbolo do elemento desejado, se precisar listar use a opção 3 do menu principal: '))

    if Tabela['Simbolo'].str.contains(sb).any():
        print(' ')
        print(Tabela[Tabela['Simbolo'] == sb])
        print(' ')
        
    else:
        print(' ')
        print('    Lista não contém elemento!')
        print(' ')


# Referência: lógica booleana e string dentro de um dataframe
# https://stackoverflow.com/questions/30944577/check-if-string-is-in-a-pandas-dataframe
