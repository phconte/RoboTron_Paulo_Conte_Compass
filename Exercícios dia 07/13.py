# Crie mais uma coluna em tempo de execução
# juntando os dados movie e year.

import pandas as pd

vencedores = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',')

vencedores['Movie_Year'] = vencedores['Movie'] + " " + vencedores['Year'].astype(str)
print(vencedores['Movie_Year'])