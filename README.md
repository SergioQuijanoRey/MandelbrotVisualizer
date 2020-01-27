
# Visualizador del conjunto de Mandelbrot

## Autor

* Sergio Quijano Rey
* sergiquijano@gmail.com
* [Página Web](sergioquijanorey.github.io)

## Descripción

Visualizamos el conjunto del Mandelbrot. Este es un conjunto de números complejos $c$ tales que la sucesión que se define a partir de ellos queda acotada:

$$z_0 = 0 \in C$$

$$z_{n+1} = z_{n}^{2} + c$$

No podemos saber si esta sucesión queda acotada, así que se procede numéricamente. Sabemos que la sucesión diverge si la norma de $z_n$ es mayor que dos. Luego podemos usar un valor de la norma mayor que 2 como criterio de divergencia (por ejemplo 10, para realzar la imagen)

Si tras un número de iteraciones dado, la sucesión queda acotada, podemos suponer que nunca divergerá.

El color de los puntos depende de la velocidad de divergencia (cuanto menor sea el $$n$$ para el cual $$z_n$$ tiene norma mayor que 2, más vivo será su color)

## Estructura

Tenemos dos programas. El primero, `mandelbrot.py`, escrito enteramente en Python. Calcula los puntos y crea la imagen usando los datos

El segundo, escrito en `C++` y `Python`. La parte de `C++`, `mandelbrot.cpp`, calcula los puntos del conjunto y los guarda en un archivo `points.csv`. La parte de `Python`, `visualizer.py`, toma el archivo con los datos y los visualiza. Esta forma de proceder no es muy eficiente, pues aunque el calcular los puntos es mucho más rápido, leer los datos consume mucho tiempo. Hace falta escribir un visualizador dentro del programa de `C++`

## Ejecución

* Hay dos programas, uno escrito enteramente en Python, y otro en C++ y Python
    * El puramente escrito en Python se ejecuta con `python3.8 mandelbrot.py`

## Resultados

**Imagen del programa Pyhton**:

![python_mandelbrot](mandelbrot.png)

**Imagen del programa en C++**:

![cpp_mandelbrot](mandelbrot_cpp.png)

## To-Do

* Hacer la visualización en C++ para evitar el script en Python que es muy lento
