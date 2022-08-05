import A
import B
import C

def main():
    print('==' * 10)


opcao = 0
while opcao != 4:
    print('''    [ 1 ] Listar uma propriedade dos elementos
    [ 2 ] Listar todos os dados de determinado elemento, buscando através do seu símbolo
    [ 3 ] Listar todos os dados de todos os elementos inseridos
    [ 4 ] Encerrar o programa''')
    opcao = int(input("    O que deseja fazer? "))
    if opcao == 1:
        A.func1()

    elif opcao == 2:
        B.func2()

    elif opcao == 3:
        C.func3()

    else:
        print('Erro! Digite uma opção válida.')
        print('==' * 10)
    print('Programa encerrado')
    break

if __name__ == '__main__':
    main()
