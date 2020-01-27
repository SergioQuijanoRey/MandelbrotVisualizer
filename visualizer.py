"""Visualiza un archivo de datos .csv generado por el programa c++ de calculo de Mandelbrot.
Author:
    - Sergio Quijano Rey
Date:
    - 27/01/2020
"""

from PIL import Image, ImageColor

# Parametros del programa
#===============================================================================
file_name = "mandelbrot_cpp.png"    # Nombre del archivo donde guardamos la imagen generada
data_file = "points.csv"        # Nombre del archivo del que tomamos los datos
width = -1                      # Anchura de la imagen
height = -1                     # Altura de la imagen

# Funcion principal
#===============================================================================
if __name__ == "__main__":
    # Carga de datos
    print("Cargando datos")
    data = []
    with open(data_file, "r") as data_file:
        data = data_file.readlines()

    # Procesamiento de los datos
    print("Procesando datos")
    data = [row.replace("\n", "") for row in data]
    data = [row.replace(" ", "") for row in data]
    data = [row.split(",") for row in data]
    data = [[int(col) for col in row] for row in data]

    # Creacion de imagen canvas
    print("Creando imagen")
    width = data[0][0]
    height = data[0][1]
    data.pop(0)

    # Dimensiones de la imagen
    image = Image.new("RGB", (width, height), "black")
    pixels = image.load()
    
    # Coloreamos la imagen
    print("Coloreando imagen")
    for row in data:
        x = row[0]
        y = row[1]
        red = row[2]
        pixels[x, y] = (red, 0, 0)

        
    # Muestra de los resultados
    image.show()
    image.save(file_name)
