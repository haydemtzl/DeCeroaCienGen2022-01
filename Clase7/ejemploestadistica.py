import pandas as pd
import numpy as np
from scipy import stats
#Creando variable que contiene mis datos del csv
readfile = pd.read_csv("notes.csv")

#Creando variables con promedio
media = readfile["nota"].mean()
mediana = readfile["nota"].median()
moda = readfile["nota"].mode()
rango = readfile["nota"].max() - readfile["nota"].min()

#Creando variables para calcular varianza y desviación estándar
arr = np.array([1,2,3,4,5,6])
arr2 = np.array([600,470,170,430,300])

media1 = np.mean(arr)
mediana1 = np.median(arr)
moda1 = stats.mode(arr)
varianza = np.var(arr)
desest = np.std(arr)

media2 = np.mean(arr2)
mediana2 = np.median(arr2)
moda2 = stats.mode(arr2)
varianza2 = np.var(arr2)
desest2 = np.std(arr2)

# print(media, mediana, moda, rango)
# print(readfile.describe())
print(media1, mediana1, moda1, varianza, desest)
print(media2, mediana2, moda2, varianza2, desest2)
