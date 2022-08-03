# Usando Pandas, procure por um dado específico 
# (da sua escolha) e printe somente o 
# mesmo utilizando o CSV.

import pandas as pd

nomes = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',')
df_aux = pd.concat([nomes['Name']])
print(df_aux[df_aux.duplicated()])


