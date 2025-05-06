import pandas as pd

df = pd.read_csv("datos.csv", names=["name","lastname","age"])

#obteniendo los datos de la columna porn nombre o name 
nombres = df["name"]

print(nombres)