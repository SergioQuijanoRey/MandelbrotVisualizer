#include <iostream>
#include <complex>
#include <fstream>
#include <cmath>
using namespace std;

// Parametros del programa
//==============================================================================
const int width = 1920;
const int height = 1080;
const int max_iteraciones = 50;
const int max_norma = 2;
const string file_name = "points.csv";

// Definicion de estructuras
//==============================================================================
typedef complex<double> complejo;

// Funciones
//==============================================================================

/**
 * Devuelve la iteracion en la que el numero se sale
 * Devuelve -1 si el numero queda acotado
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

int get_red_by_iterations(complejo c){
    int iteracion = get_mandelbrot_iteration(c);
    int red = ((double)(iteracion) / (double)max_iteraciones) * 255;
    return red;
}

/**
 * x tiene que estar en [-2.5, 1]
 * */
double map_pixel_to_x(int pixel_x){
    double x = ((double)pixel_x / (double)width) * 3.5 - 2.5;
    return x;
}

/**
 * y tiene que estar en [-1, 1]
 * */
double map_pixel_to_y(int pixel_y){
    double y = ((double)pixel_y / (double)height) * 2 - 1;
    return y;
}

int main(){
    ofstream output;
    output.open(file_name.c_str());

    // Guardo en el archivo las dimensiones de la imagen
    output << width << ", " << height << endl;

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

    output.close();

    cout << "Todo va bien" << endl;

}
