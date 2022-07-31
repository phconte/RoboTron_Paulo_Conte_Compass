# Construa um programa que recebe 20 valores para X e no final apresenta a média aritmética dos valores pares digitados

# Solicita até 20 valores
print("Informe um total de 20 valores")
x = [float(input("Número: ")) for i in range(20)]

# Armazena numa lista somente os numeros pares
pares = []
for valor_pares in x:
    if valor_pares % 2 == 0:
        pares.append(valor_pares)

# Confere se a quantidade de valores na lista não é 0
if len(pares) == 0:
    print("Nenhum valor par informado!")
# Apresenta quais os valores pares foram informados, soma esses valores e divide pelo n de valores
else:
    print("Os valores pares informados são:", pares)
    print("A média aritmética entre eles é:", sum(pares) / len(pares))


# Referências
#
# Como receber 20 valores:
# https://pt.stackoverflow.com/questions/203676/uma-lista-para-receber-20-n%C3%BAmeros-inteiros-e-armazenar-em-uma-lista-e-imprimir-o
#
# Como extrair somente valores pares de uma lista:
# https://pt.stackoverflow.com/questions/366275/a-partir-de-uma-lista-devolver-os-n%C3%BAmeros-pares-em-python
#
# Contar valores numa lista:
# https://www.delftstack.com/pt/howto/python/count-elements-in-list-python/
#
# Somar valores numa lista:
# https://www.delftstack.com/pt/howto/python/sum-of-list-of-numbers-in-python/
