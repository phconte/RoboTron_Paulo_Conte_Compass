# Construa um programa que armazena uma idade em uma váriavel e compara, 
# se a idade for maior que 18, apresenta "Maior de idade", se a idade for menor que 12, 
# apresenta "Você é uma criança" e se for maior que 12 e menor que 18, apresenta "Você é um adolescente"

idade = int(input("Para saber se você é criança, adolescente ou adulto, informe a idade: "))

if idade >= 18:
    print("Você é maior de idade")
elif idade < 12:
    print("Você é uma criança")
else:
    print("Você é adolescente")