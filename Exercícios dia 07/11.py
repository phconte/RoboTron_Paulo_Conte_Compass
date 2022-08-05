# Printe o nome do Ator que ganhou o Oscar em 1993

import pandas as pd

vencedor = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',')
vencedor_93 = (vencedor.loc[vencedor['Year'] == 1993])

nome_vencedor = pd.DataFrame(vencedor_93, columns=['Name'])

print("O vencedor do Oscar em 1993 foi:")
print(nome_vencedor.to_string(index=False))
