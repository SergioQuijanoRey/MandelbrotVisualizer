from PIL import Image, ImageColor

# Parametros del programa
#===============================================================================
file_name = "mandelbrot.png"
data_file = "points.csv"
width = -1
height = -1

# Funcion principal
#===============================================================================
if __name__ == "__main__":
    # Carga de datos
    print("Cargando datos")
    data = []
    with open(data_file, "r") as data_file:
        data = data_file.readlines()

    print("Procesando datos")
    data = [row.replace("\n", "") for row in data]
    data = [row.replace(" ", "") for row in data]
    data = [row.split(",") for row in data]
    data = [[int(col) for col in row] for row in data]

    print("Creando imagen")
    # Creacion de imagen canvas
    width = data[0][0]
    height = data[0][1]
    data.pop(0)

    # Tomar las dimensiones de la imagen
    image = Image.new("RGB", (width, height), "black")
    pixels = image.load()
    
    print("Coloreando imagen")
    # Coloreamos la imagen
    for row in data:
        x = row[0]
        y = row[1]
        red = row[2]
        pixels[x, y] = (red, 0, 0)

        
    # Muestra de los resultados
    image.show()
    image.save(file_name)
