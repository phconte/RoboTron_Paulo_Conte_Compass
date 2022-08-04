# Mostre todos os filmes menos o “The Revenant”

import pandas as pd

vencedores = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',')
movies = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',', usecols=['Movie'])

print(movies[movies['Movie'] != "The Revenant"])
