# Crie um programa que lê 1 valor inteiro para X. Se o valor for par, calcular
# o fatorial de x em uma função e apresentar o resultado fora da função.
# Se o valor for impar, apresentar em uma função a tabuada de 1 a 10 de X.

# Função fatorial, verifica se o valor não é negativo
def fatorial(n):
    if x >= 0:
        f = 1
        for i in range(n, 0, -1):
            f = f * i
        print("A fatorial de", x, "é", f)
    else:
        print("O número é par mas não existe fatorial para número negativo")


# Função para tabuada
def tabuada(n):
    print("Neste caso a tabuada do valor ímpar é:")
    for i in range(1, 11):
        m = i * n
        print(n, "x", i, "=", m, end=", ")


# Solicita um valor inteiro e verificar se é par ou ímpar
x = int(input("Informe um valor inteiro: "))
if x % 2 == 0:
    print(fatorial(x))
else:
    tabuada(x)


# Referência de como fazer fatorial em uma função https://www.youtube.com/watch?v=84jUX96cs7Q
