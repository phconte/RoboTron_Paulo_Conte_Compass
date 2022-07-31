# Construa um programa que armazena em duas variaveis duas notas e apresenta a média entre as duas

# Solicitando os valores
Nota_sprint_01 = float(input("Informe a nota da Sprint 01: "))
Nota_sprint_02 = float(input("Informe a nota da Sprint 02: "))

# Somando as notas e dividindo por 2
Media = (Nota_sprint_01 + Nota_sprint_02) / 2
# Mostrando o resultado que deverá ser com no máximo duas casas após o ponto
print("A nota media das Sprints é: %.2f" % Media)

# Referência para aprender como usar limite de casa decimal:
# https://stackoverflow.com/questions/67450190/can-someone-tell-me-what-1f-means
