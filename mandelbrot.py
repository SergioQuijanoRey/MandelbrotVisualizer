from PIL import Image, ImageColor
import cmath
import math

# Parametros del programa
#===============================================================================
witdh = 1920
height = 1080
max_iteraciones = 50
max_norma = 2
file_name = "mandelbrot.png"

# Funciones auxiliares
#===============================================================================
def map_pixel_x(x):
    return (x / witdh) * 3.5 - 2.5

def map_pixel_y(y):
    return (y / height) * 2 - 1

def get_red_mandelbrot(x, y):
    iteration = get_iteration_mandelbrot(x, y)
    return int((iteration / max_iteraciones) * 255)

def norma(z):
    return math.sqrt(z.real*z.real + z.imag*z.imag)


# x: parte real
# y: parte compleja
def get_iteration_mandelbrot(x, y):
    c = complex(x, y)
    z = complex(0, 0)
    current_iteration = 0

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
    image = Image.new("RGB", (witdh, height), "black")
    pixels = image.load()

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            new_x = map_pixel_x(x)
            new_y = map_pixel_y(y)
            red = get_red_mandelbrot(new_x, new_y)

            pixels[x, y] = (red, 0, 0)

    
    image.show()
    image.save(file_name)
