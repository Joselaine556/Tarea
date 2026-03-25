
## Resumen general  

En este análisis trabajé con el dataset Iris, que contiene información sobre distintas flores.  

El objetivo fue observar cómo cambian las medidas de los pétalos y los sépalos dependiendo de la especie, y ver si se pueden diferenciar fácilmente.
En total hay **150 registros**.

---

## Promedios por especie

Esta tabla muestra el tamaño promedio de los pétalos y sépalos en cada especie.


| variety    |   sepal.length |   sepal.width |   petal.length |   petal.width |
|:-----------|---------------:|--------------:|---------------:|--------------:|
| Setosa     |           5.01 |          3.43 |           1.46 |          0.25 |
| Versicolor |           5.94 |          2.77 |           4.26 |          1.33 |
| Virginica  |           6.59 |          2.97 |           5.55 |          2.03 |

---

##  Hallazgos importantes  

Después de observar la tabla se puede notar varias diferencias entre las especies.

- La especie con mayor tamaño promedio de pétalo es **Virginica**  
- La especie con menor tamaño promedio de pétalo es **Setosa**  
- La especie con mayor variabilidad en pétalos es **Virginica**  

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

La especie **Setosa** es la que tiene los pétalos más pequeños, por lo que se hace más fácil de identificar.  
Por otro lado, **Virginica** es la que tiene los pétalos más grandes.  
La otra especie queda como en un punto intermedio, ya que no es ni tan pequeña ni tan grande como las demás.
