# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo,sabendo que o mesmo
# pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
# Entrada: A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.
# Saída: Apresente a duração do jogo conforme exemplo abaixo

inicial, final = map(int, input(
    'Informe a hora inicial e a hora final, usando formato 24h:  ').split())
tempo = final - inicial

if tempo < 0:
    print("A duração do jogo foi de:", tempo + 24, "horas.")
elif tempo == 0:
    print("A duração do jogo foi de 24 horas.")
else:
    print("A duração do jogo foi de:", tempo, "horas.")


# Referência para usar map e split:
# https://pt.stackoverflow.com/questions/427259/%C3%89-poss%C3%ADvel-incluir-mais-de-uma-vari%C3%A1vel-por-input-no-python
