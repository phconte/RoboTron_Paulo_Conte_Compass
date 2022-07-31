# Crie um programa que recebe 15 valores e armazena em uma lista, e no final da execução mostre os valores da lista do ultimo para o primeiro

# Solicita 15 valores
print("Informe um total de 15 valores")
lista = [float(input("Número: ")) for i in range(15)]

# Reverte a ordem dos valores e mostra
lista.reverse()
print("A lista invertida é:", lista)

# Referência de como inverter lista https://www.programiz.com/python-programming/methods/list/reverse
