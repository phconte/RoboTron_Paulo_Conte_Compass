# Crie uma “aplicação” em loop que tenha uma opção para listar todos os
# elementos da tabela, porém mostrando apenas uma propriedade do elemento.
# Ex: listar todos os nomes dos elementos na tabela.

def func1():
    print('==' * 10)

    import pandas as pd


    simbolo_csv = pd.read_csv('Tabela.csv', encoding='UTF-8',
                            sep=',', usecols=['Simbolo'])
    Nome_csv = pd.read_csv('Tabela.csv', encoding='UTF-8',
                        sep=',', usecols=['Nome'])
    NumeroAtomico_csv = pd.read_csv(
        'Tabela.csv', encoding='UTF-8', sep=',', usecols=['NumeroAtomico'])
    Linha_csv = pd.read_csv('Tabela.csv', encoding='UTF-8',
                            sep=',', usecols=['Linha'])
    Coluna_csv = pd.read_csv('Tabela.csv', encoding='UTF-8',
                            sep=',', usecols=['Coluna'])
    EstadoFisico_csv = pd.read_csv(
        'Tabela.csv', encoding='UTF-8', sep=',', usecols=['EstadoFisico'])

    opcao = 0
    while opcao != 7:
        print('''        [ 1 ] Listar Simbolos
        [ 2 ] Listar Nome
        [ 3 ] Listar Numero Atomico
        [ 4 ] Listar Linha
        [ 5 ] Listar Coluna
        [ 6 ] Listar Estado Fisico
        [ 7 ] Retornar Menu Principal''')
        print('    ====================')
        opcao = int(input("    O que deseja fazer? "))
        if opcao == 1:
            print(simbolo_csv)
            print('==' * 10)

        elif opcao == 2:
            print(Nome_csv)
            print('==' * 10)

        elif opcao == 3:
            print(NumeroAtomico_csv)
            print('==' * 10)

        elif opcao == 4:
            print(Linha_csv)
            print('==' * 10)

        elif opcao == 5:
            print(Coluna_csv)
            print('==' * 10)

        elif opcao == 6:
            print(EstadoFisico_csv)
            print('==' * 10)

        elif opcao == 7:
            print('Retornando')
            print('==' * 10)
            break

        else:
            print('Erro! Digite uma opção válida.')
            print('==' * 10)
            
# Referência: criar menus com loop
# https://www.youtube.com/watch?v=OBJL5vPj4-E
