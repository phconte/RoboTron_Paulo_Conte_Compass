# Printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016

import pandas as pd

vencedor = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',')
vencedor_91 = (vencedor.loc[vencedor['Year'] == 1991])
vencedor_16 = (vencedor.loc[vencedor['Year'] == 2016])

nome_vencedor_91 = pd.DataFrame(vencedor_91, columns=['Name'])
nome_vencedor_16 = pd.DataFrame(vencedor_16, columns=['Name'])

print("Os vencedores do Oscar entre 1991 e 2016 foram:")
print(nome_vencedor_91.to_string(index=False))
print(nome_vencedor_16.to_string(index=False))
