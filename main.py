import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Para abrir el archivo JSON
with open("data/iris.json") as f:
    data = json.load(f)
df = pd.DataFrame(data)

#Resumen del dataset
print("Número de registros:", len(df))
print("Columnas:", df.columns)
print("\nVariables existentes:")


print(df.head())
tabla_estadistica = df[[
    "sepal.length",
    "sepal.width",
    "petal.length",
    "petal.width"
]].agg(["mean", "min", "max"]).round(2)

# Resumen por especie
resumen = df.groupby("variety").agg({
    "sepal.length": ["mean", "min", "max"],
    "sepal.width": ["mean", "min", "max"],
    "petal.length": ["mean", "min", "max"],
    "petal.width": ["mean", "min", "max"]
})

resumen.columns = [
    col[0].replace(".", " ").title() + " (" + col[1].capitalize() + ")"
    for col in resumen.columns
]

resumen = resumen.reset_index()
resumen = resumen.round(2)

print("\nResumen por especie:")
print(resumen)

promedios = df.groupby("variety").mean().round(2)



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
mayor_sepal = promedios["sepal.length"].idxmax()

reporte = f"""
## Resumen general  

En este análisis trabajé con el dataset Iris, que contiene información sobre distintas flores.  

El objetivo fue observar cómo cambian las medidas de los pétalos y los sépalos dependiendo de la especie, y ver si se pueden diferenciar fácilmente.
En total hay **{len(df)} registros**.

---

## Estadísticas generales

{tabla_estadistica.to_markdown()}

Esta tabla muestra un resumen general de las medidas del dataset, permitiendo ver los valores promedio, mínimos y máximos.

---

## Resumen por especie

{resumen.to_markdown(index=False)}

Esta tabla permite comparar las características de cada especie, mostrando cómo cambian las medidas de pétalos y sépalos.

---

##  Hallazgos importantes  

Después de observar la tabla se puede notar varias diferencias entre las especies.

- La especie con mayor tamaño promedio de pétalo es **{mayor_petalo}**  
- La especie con menor tamaño promedio de pétalo es **{menor_petalo}**  
- La especie con mayor variabilidad en pétalos es **{mas_variable}**  
- La especie con mayor tamaño de sépalo es **{mayor_sepal}**   

En general, el tamaño del pétalo es una de las variables que más ayuda a diferenciar las especies.  
También se puede notar que algunas especies son muy fáciles de distinguir, mientras que otras son más parecidas entre sí.


---

## Información de las especies  

### Setosa  
Es la más pequeña y fácil de identificar.

### Versicolor  
Tiene tamaño intermedio y puede confundirse más.

### Virginica  
Es la más grande y destaca por sus pétalos largos.

### Promedio de longitud de pétalos  
![Promedio de pétalos](../Visualizaciones/petal_promedio.png)

Este gráfico muestra el promedio de la longitud de los pétalos para cada especie de flor.

---

### Promedio del largo del sépalo  
![Promedio del sépalo](../Visualizaciones/sepal_promedio.png)

Aquí se puede ver que el tamaño del sépalo también cambia dependiendo de la especie.

---

### Relación entre largo y ancho del sépalo  
![Relación del sépalo](../Visualizaciones/sepal_scatter.png)

En este gráfico se observa la relación entre el largo y el ancho del sépalo. Los puntos están coloreados por especie, lo que permite ver cómo se agrupan las flores.


## Conclusión
Después de analizar los datos, pude notar que sí hay diferencias claras entre las especies del dataset Iris.

La especie **{menor_petalo}** es la que tiene los pétalos más pequeños, por lo que se hace más fácil de identificar.  
Por otro lado, **{mayor_petalo}** es la que tiene los pétalos más grandes.  
La otra especie queda como en un punto intermedio, ya que no es ni tan pequeña ni tan grande como las demás.
"""
with open("Reporte/reporte.md", "w", encoding="utf-8") as f:
    f.write(reporte)

print("Reporte generado")