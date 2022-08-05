import A
import B
import C


def main():
    print('==' * 50)


opcao = 0
while opcao != 4:
    print('==' * 50)
    print('''    
    Bem vindo a Tabela Periódica do Paulo.
    Aqui serão listados até 15 elementos da tabela.
    Você tem 3 formas de exibi-las:
    [ 1 ] Listar uma propriedade dos elementos
    [ 2 ] Listar todos os dados de determinado elemento, buscando através do seu símbolo
    [ 3 ] Listar todos os dados de todos os elementos inseridos
    [ 4 ] Encerrar o programa
    ''')
    print('==' * 50)
    opcao = int(input("    Escolha uma das opções: "))
    if opcao == 1:
        A.func1()

    elif opcao == 2:
        B.func2()

    elif opcao == 3:
        C.func3()
    
    elif opcao == 4:
        print(' ')
        print('    Finalizando.')
        break

    else:
        print(' ')
        print('    Erro, digite uma opção válida!')
        print('==' * 50)
        print(' ')

print('    Programa encerrado!')
print('    Obrigado e volte sempre! :D')
print(' ')
print('==' * 50)
print(' ')
