#  Listar todos os dados de todos os elementos inseridos.

import pandas as pd


def func3():
    print(' ')
    print('==' * 50)
    print(' ')
    arquivo = pd.read_csv('Tabela.csv', encoding='UTF-8', sep=',')
    print(arquivo)
    print(' ')
