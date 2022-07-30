# Construa um programa que recebe 20 valores para X e no final apresenta a média aritmética dos valores pares digitados
print("Informe um total de 20 valores")
x = [float(input("Número: ")) for i in range(20)]

pares = []
for valorPares in x:
    if valorPares % 2 == 0:
        pares.append(valorPares)

if len(pares) == 0:
    print("Nenhum valor par informado!")
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
