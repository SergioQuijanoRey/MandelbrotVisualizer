/**
 * @file mandelbrot.cpp
 * @author Sergio Quijano Rey
 * @brief Calcula el conjunto de Mandelbrot. Los datos los guarda en un archivo
 *        .csv para que sea visualizado por un script de python
 * */
#include <iostream>
#include <complex>
#include <fstream>
#include <cmath>
using namespace std;

// Parametros del programa
//==============================================================================
const int width = 1920;                     // Anchura de la imagen
const int height = 1080;                    // Altura de la imagen
const int max_iteraciones = 50;             // Cota de numero de iteraciones
const int max_norma = 2;                    // Cota de la norma
const string file_name = "points.csv";      // Archivo donde se almacenan los resultados

// Definicion de estructuras
//==============================================================================
typedef complex<double> complejo;   // Complejo usando double

// Funciones
//==============================================================================

/**
 * @brief Calcula las iteraciones que tarda un numero complejo en diverger
 * @param c el complejo sobre el que se realizan los calculos
 * @return el numero de iteraciones que tarda en diverger
 *         Si no diverge, se devuelve el numero maximo de iteraciones
 * Consideramos que la sucesion diverge cuando su norma es mayor que @max_norma
 * */
int get_mandelbrot_iteration(complejo c){
    complejo z = complejo(0,0);
    int current_iteration = 0;

    while(norm(z) < max_norma && current_iteration < max_iteraciones){
        z = z*z + c;
        current_iteration = current_iteration + 1;
    }

    return current_iteration;
}

/**
 * @brief Calcula el valor del rojo segun la divergencia de la sucesion de Mandelbrot
 * @param c complejos sobre el que se realizan los calculos
 * @return un numero entero en el intervalo [0, 255], segun la velocidad de divergencia
 * */
int get_red_by_iterations(complejo c){
    int iteracion = get_mandelbrot_iteration(c);
    int red = ((double)(iteracion) / (double)max_iteraciones) * 255;
    return red;
}

/**
 * @brief Mapea un pixel a un valor del intervalo [-2.5, 1]
 * @param pixel_x, el valor horizontal del pixel a mapear
 * @return un valor en el intervalo dado
 * */
double map_pixel_to_x(int pixel_x){
    double x = ((double)pixel_x / (double)width) * 3.5 - 2.5;
    return x;
}

/**
 * @brief Mapea un pixel a un valor del intervalo [-1, 1]
 * @param pixel_y el valor vertical del pixel a mapear
 * @return un valor en el intervalo dado
 * */
double map_pixel_to_y(int pixel_y){
    double y = ((double)pixel_y / (double)height) * 2 - 1;
    return y;
}

// Funcion principal
//==============================================================================
int main(){
    // Archivo de escritura
    ofstream output;
    output.open(file_name.c_str());

    // Guardo en el archivo las dimensiones de la imagen
    output << width << ", " << height << endl;

    // Calculo de los valores de todos los pixeles
    clog << "Calculando valores de los pixeles" << endl;
    for(int i = 0; i < width; i++){
        for(int j = 0; j < height; j++){

            // Mapeo los pixeles al plano complejo
            double x = map_pixel_to_x(i);
            double y = map_pixel_to_y(j);

            complejo current_complejo = complejo(x, y);
            int red = get_red_by_iterations(current_complejo);

            output << i << ", " << j << ", " << red << endl;

            // Comprobacion de escritura
            if(!output){
                 cerr << "ERROR: escribiendo en el archivo para el pixel " << i << ", " << j << endl;
            }
        }
    }
    clog << "Valores calculados" << endl;

    // Comprobacion de escritura
    if(!output){
         cerr << "ERROR: en el proceso global" << endl;
    }

    // Fin del programa
    output.close();
    cout << "Todo va bien" << endl;
    return 0;
}
