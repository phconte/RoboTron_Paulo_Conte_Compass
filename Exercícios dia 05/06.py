# Construa um programa que receba um valor inteiro maior que 2 em uma variavel x e apresenta os impares entre 0 e x

# Solicita o valor maior que 2
x = int(input("Informe um valor inteiro maior que 2: "))

# Confere se o valor informado é maior que
if x <= 2:
    print("Valor deve ser maior que 2!")
# Se for maior que 2, armazena numa lista de 2 em 2, começando no 3
else:
    print("Os valores ímpares entre 3 e", x, "são:")
    x = range(3, x+1, 2)
    for i in x:
        print(i, end=", ")


# Referências
#
# Para uso do range():
# https://pynative.com/python-range-function/
#
# Para apresentar valores na mesma linha:
# https://stackoverflow.com/questions/18424899/print-range-of-numbers-on-same-line
