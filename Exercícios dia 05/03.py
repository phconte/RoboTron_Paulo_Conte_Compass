# Construa um programa que recebe dois valores, soma esses valores e apresenta se o resultado é par ou impar

# Solicitando os valores
print("Para saber se o valor é par ou impar, informe:")
Valor01 = int(input("O primeiro valor: "))
Valor02 = int(input("O segundo valor: "))

# Somando os valores
soma = Valor01 + Valor02

# Verificando se o resto da divisão é 0
if soma % 2 == 0:
    print("O numero", soma, "é par!")
# Se não for 0 ele será ímpar
else:
    print("O numero", soma, "é ímpar!")

# Referência para saber se é par ou ímpar:
# https://www.pythonprogressivo.net/2018/03/Saber-Numero-Par-Impar-Python.html
