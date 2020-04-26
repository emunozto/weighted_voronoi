# Voronoi ponderado para soccer
Un diagrama de Voronoi es una construcción geométrica que nos permite particionar el campo de soccer en regiones, estas regiones son llamadas regiones de dominio.
Un diagrama de Voronoi crea celdas delimitadas por un poligono, utiliza la distancia para asignar una region de dominio al jugador mas cercano.

El diagrama de Voronoi ponderado es una variación del diagrama clásico de Voronoi, en donde se agrega una funcion de peso $w$, la cual nos ayuda a controlar el nivel de influencia que un jugador puede tener sobre cierta celda. Cada celda puede ser expresada como

![](equation.png)

Una función de peso típica es ![](w.png), en donde $d$ es la distancia del jugador $i$ a un punto específico en el campo $m$, ![](beta.png) puede ser una constante.

El Voronoi estima el espacio dominado por cada equipo considerando únicamente la distancia, mientras que el Voronoi ponderado puede ser modificado para considerar otros parámetros dependientes del tiempo.

Código Fuente
* `voronoi_weighted.py`: Este script contiene la visualización y las funciones de cálculos del Vorionoi ponderado.
* `tutorial_voronoi_weighted.ipynb`: Este notebook muestra como utilizar el `voronoi_weighted.py`.