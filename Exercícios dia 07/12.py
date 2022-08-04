# Printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016

import pandas as pd

vencedores = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',')
vencedor_periodo = (vencedores.loc[63:88])
print(vencedor_periodo)

nome_vencedor = pd.DataFrame(vencedor_periodo, columns=['Name'])

print("Os vencedores do Oscar entre 1991 e 2016 foram:")
print(nome_vencedor)