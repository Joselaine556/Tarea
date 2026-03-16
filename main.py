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

reporte = f"""
# Reporte de análisis del dataset Iris

## ¿Qué información útil nos dan los datos?
Los datos permiten ver las diferencias entre las especies de flores Iris a partir de las medidas de sus pétalos y sépalos. 
Con los gráficos y las estadísticas se puede observar que algunas especies tienen pétalos más largos o más anchos que otras. 
Esto ayuda a comparar las especies y entender mejor sus características.

## Promedio de longitud de pétalos por especie

![Promedio de pétalos](Visualizaciones/petal_promedio.png)

Este gráfico muestra el promedio de la longitud de los pétalos para cada especie de flor.

---

## Promedio del largo del sépalo por especie

![Promedio del sépalo](Visualizaciones/sepal_promedio.png)

Aquí se puede ver que el tamaño del sépalo también cambia dependiendo de la especie.

---

## Relación entre largo y ancho del sépalo por especie

![Relación del sépalo](Visualizaciones/sepal_scatter.png)

En este gráfico se observa la relación entre el largo y el ancho del sépalo. Los puntos están coloreados por especie, lo que permite ver cómo se agrupan las flores.


## Conclusión
En general, se pueden notar diferencias entre las especies de Iris en el tamaño de sus pétalos y sépalos. 
Estas medidas ayudan a distinguir cada tipo de flor.
"""
with open("Reporte/reporte.md", "w", encoding="utf-8") as f:
    f.write(reporte)

print("Reporte generado")