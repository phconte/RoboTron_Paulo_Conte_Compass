# Crie um programa que contêm uma função que receba dois parâmetros inteiros e retorna a média dos dois valores

def operador(n1, n2):
    soma = n1 + n2
    div = soma / 2
    return soma, div


n1 = int(input("Informe o primeiro parâmetro inteiro: "))
n2 = int(input("Informe o segundo parâmetro inteiro: "))

soma, div = operador(n1, n2)

print("A média dos parâmetros é: %.2f" % div)

# Referência para função https://www.codingem.com/python-how-to-return-multiple-values/
