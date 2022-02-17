import pandas as pd

readfile = pd.read_csv("notes.csv")

media = readfile["numero"].mean()
mediana = readfile["numero"].median()
moda = readfile["numero"].mode()

rango = readfile["numero"].max() - readfile["numero"].min()

print(media, mediana, rango)
