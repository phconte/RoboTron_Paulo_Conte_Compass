# Usando Pandas, leia apenas os dados da coluna Age do CSV

import pandas as pd

age = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',', usecols=['Age'])
print(age)

