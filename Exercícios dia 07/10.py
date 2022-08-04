# Usando Pandas, procure por um dado específico
# (da sua escolha) e printe somente o
# mesmo utilizando o CSV.

import pandas as pd

vencedores = pd.read_csv('CSV.csv', encoding='UTF-8',
                         sep=',', usecols=['Name', 'Movie', 'Year'])
print("Os primeiros 10 vencedores do Oscar de melhor ator foram:")
print(vencedores.loc[0:9])
