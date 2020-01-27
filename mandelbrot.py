"""Visualiza el conjunto de Mandelbrot.

Author:
    - Sergio Quijano Rey
Date:
    - 27/01/2020

El conjunto de Mandelbrot son aquellos puntos $c$ del plano complejo tales que la
siguente sucesión queda acotada:

    $z_0 = 0 \in \mathds{C}$
    $z_{n+1} = z_{n}^{2} + c$

Como no podemos saber si esta acotada, hacemos un numero de iteraciones. Si el 
modulo de $z_n$ es menor que dos, suponemos que esta acotada. Si en algun momento
dicho modulo es mayor que dos, sabemos que la sucesion no esta acotada. Se puede
utilizar una cota mayor para que la imagen sea realzada

"""

from PIL import Image, ImageColor
import cmath
import math

# Parametros del programa
#===============================================================================
witdh = 1920                        # Anchura de la imagen
height = 1080                       # Altura de la imagen
max_iteraciones = 50                # Cota para las iteraciones
max_norma = 10                      # Cota para la norma
file_name = "mandelbrot.png"        # Archivo donde se guarda la imagen generada

# Funciones auxiliares
#===============================================================================
def map_pixel_to_complex(x, y):
    """Mapea un pixel al plano complejo. 

    Parameters:
        - x: posicion horizontal del pixel
        - y: posicion vertical del pixel
    Returns:
        - Dos parametros a,b
            a: parte real del complejo, a se mueve en [-2.5, 1]
            b: parte imaginaria del compejo, b se mueve en [-1, 1]
            
    Esto se hace para que la imagen del conjunto quede centrada

    """

    return (x / witdh) * 3.5 - 2.5, (y / height) * 2 - 1

def get_red_mandelbrot(x, y):
    """Devuelve el valor de rojo de un valor complejo.
    
    Parameters:
        - x: la parte real del complejo
        - y: la parte imaginaria del complejo
    Returns:
        - Un valor entero en el intervalo [0, 255] que indica la intensidad del rojo

    """

    iteration = get_iteration_mandelbrot(x, y)
    return int((iteration / max_iteraciones) * 255)

def norma(z):
    """Calcula la norma de un numero complejo

    Parameters:
        - z: el numero complejo
    Returns:
        - La norma de z

    """
    return math.sqrt(z.real*z.real + z.imag*z.imag)


def get_iteration_mandelbrot(x, y):
    """Calcula el numero de iteraciones que tarda un numero complejo en diverger en la sucesion de Mandelbrot.

    Parameters: 
        - x: la parte real del complejo
        - y: la parte imaginaria del complejo
    Returns:
        - El numero de iteraciones que tarda en diverger
        - Si no diverge, se devuelve -1

    """
    # Se crea el complejo y la primera iteracion de la sucesion
    c = complex(x, y)
    z = complex(0, 0)
    current_iteration = 0

    # Se hacen las iteraciones de la sucesion
    while current_iteration < max_iteraciones and norma(z) < max_norma:
        z = z * z + c
        current_iteration = current_iteration + 1

    if current_iteration == max_iteraciones:
        return -1
    else:
        return current_iteration


# Programa principal
#===============================================================================
if __name__ == "__main__":

    # Creamos la imagen sobre la que vamos a pintar
    image = Image.new("RGB", (witdh, height), "black")
    pixels = image.load()

    # Pintamos la imagen pixel a pixel
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            # Se mapea el pixel al plano complejo
            new_x, new_y= map_pixel_to_complex(x, y)

            # Se calcula la intensidad del rojo
            red = get_red_mandelbrot(new_x, new_y)

            # Se pinta el pixel
            pixels[x, y] = (red, 0, 0)

    
    # Se muestra y guarda la imagen
    image.show()
    image.save(file_name)
