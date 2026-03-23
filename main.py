import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Para abrir el archivo JSON
f = open("data/iris.json")
data = json.load(f)
f.close()

df = pd.DataFrame(data)

#Resumen del dataset
print("Número de registros:", len(df))
print("Columnas:", df.columns)
print("\nVariables existentes:")


print(df.head())

print("\nResumen estadistico del dataset:")
print(df.describe())

resumen = df.groupby("variety").agg({
    "sepal.length": ["mean", "min", "max"],
    "sepal.width": ["mean", "min", "max"],
    "petal.length": ["mean", "min", "max"],
    "petal.width": ["mean", "min", "max"]
})

resumen.columns = ['_'.join(col) for col in resumen.columns]
resumen = resumen.reset_index()

print("\nResumen por especie:")
print(resumen)

promedios = df.groupby("variety").mean()

plt.figure()
plt.bar(promedios.index, promedios["petal.length"])
plt.title("Promedio de longitud de pétalos por especie")
plt.ylabel("Longitud")
plt.tight_layout()
plt.savefig("Visualizaciones/petal_promedio.png")
plt.close()

# Promedio de sépalo
plt.figure()
plt.bar(promedios.index, promedios["sepal.length"])
plt.title("Promedio del largo del sépalo por especie")
plt.ylabel("Largo del sépalo")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Visualizaciones/sepal_promedio.png")
plt.close()

# Scatter
sns.scatterplot(x="sepal.length", y="sepal.width", hue="variety", data=df)
plt.title("Relación entre largo y ancho del sépalo")
plt.tight_layout()
plt.savefig("Visualizaciones/sepal_scatter.png")
plt.close()

mayor_petalo = promedios["petal.length"].idxmax()
menor_petalo = promedios["petal.length"].idxmin()

variabilidad = df.groupby("variety")["petal.length"].std()
mas_variable = variabilidad.idxmax()

reporte = f"""
##Resumen general  
Este análisis se basa en mediciones de flores Iris.  
En total hay **{len(df)} registros**.

---

##  Estadísticas por especie  

{resumen.to_markdown(index=False)}

---

##  Hallazgos importantes  

- La especie con mayor tamaño promedio de pétalo es **{mayor_petalo}**  
- La especie con menor tamaño promedio de pétalo es **{menor_petalo}**  
- La especie con mayor variabilidad en pétalos es **{mas_variable}**  

---

## Información de las especies  

### Setosa  
Es la más pequeña y fácil de identificar.

### Versicolor  
Tiene tamaño intermedio y puede confundirse más.

### Virginica  
Es la más grande y destaca por sus pétalos largos.

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