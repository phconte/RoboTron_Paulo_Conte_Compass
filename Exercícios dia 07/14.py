# Printe todos os nomes e as idades 
# dos atores que ganharam o oscar de 1987 até 1999.

import pandas as pd

vencedores = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',')

print(vencedores['Name'][59:72] + " " + vencedores['Year'][59:72].astype(str))
