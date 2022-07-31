# Crie um programa que recebe uma lista com três frutas e compare com uma lista com os valores ["maça", "banana", "pera"]

# Lista de compras da semana
lista_compras = ['maça', 'banana', 'pera']

# Solicita quais frutas tinham no mercado
estoque_mercado = [str(input("Quais frutas foram compradas: "))
                   for i in range(3)]

# Compara as listas
iguais = [fruta for fruta in lista_compras if fruta in estoque_mercado]

# Se nenhuma fruta for igual
if len(iguais) == 0:
    print("Nenhuma fruta encontrada!")

# Se não informa quais frutas são iguais
else:
    print("Riscar da lista de compras:", iguais)


# Referência para comparar listas https://pt.stackoverflow.com/questions/490489/comparar-duas-listas-em-python-e-retornar-correspond%C3%AAncias
