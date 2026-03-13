import json
import pandas as pd

# Para abrir el archivo JSON
f = open("data/iris.json")
data = json.load(f)
f.close()

df = pd.DataFrame(data)

print("Número de registros:", len(df))
print("Columnas:", df.columns)
print("\nPrimer registro:")
print(data[0])

print(df.head())