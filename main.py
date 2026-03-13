import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Para abrir el archivo JSON
f = open("data/iris.json")
data = json.load(f)
f.close()

df = pd.DataFrame(data)

#Resumen del dataset
print("Número de registros:", len(df))
print("Columnas:", df.columns)
print("\nVariables existentes:")
print(list(data[0].keys()))


print(df.head())

print("\nResumen estadistico del dataset:")
print(df.describe())

print("\nEstadísticas por especie:")
print(df.groupby("variety").describe())

promedio = df.groupby("variety")["petal.length"].mean()

#Promedio de pétalos por especie
plt.figure(figsize=(6,4))
plt.bar(promedio.index, promedio.values)
plt.title("Promedio de longitud de pétalos por especie")
plt.ylabel("Longitud")
plt.tight_layout()
plt.savefig("Visualizaciones/petal_promedio.png")

df.groupby("variety")["sepal.length"].mean().plot(kind="bar")

plt.title("Promedio del largo del sépalo por especie")
plt.ylabel("Largo del sépalo")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("Visualizaciones/sepal_promedio.png")
plt.clf()

#Relación entre largo y ancho del sépalo por especie
sns.scatterplot(x="sepal.length", y="sepal.width", hue="variety", data=df)

plt.title("Relación entre largo y ancho del sépalo")
plt.tight_layout()

plt.savefig("Visualizaciones/sepal_scatter.png")
plt.clf()