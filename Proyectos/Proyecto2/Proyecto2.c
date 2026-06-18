#include <stdio.h>
#include <stdlib.h> //Se utiliza para generacion de numeros random
#include <time.h> //Asegura numeros distintos en cada ejecucion
#include <stdbool.h> //Para retornar valor booleano True en funcion auto-home

struct Eslabon_brazo { // Define estructura de eslabon con su id y posiciones x e y
    int id;
    float pos_x;
    float pos_y;
};

// Funcion para generar posiciones iniciales (sobreescribe valor de pos_x y pos_y)
float pos_inicial(float *pos_x, float *pos_y) {
    *pos_x = ((float)rand() / RAND_MAX) * 360.0; //RAND_MAX es una constante definida por la libreria stdlib.h
    *pos_y = ((float)rand() / RAND_MAX) * 360.0;
   
    return 1.0; //Indica que la funcion se ejecuto con exito (se coloca 1.0 para cumplir con el float que se puso al inicio)
}

bool auto_home(struct Eslabon_brazo *eslabon) { // eslabon es "variable auxiliar" especifica de la funcion. Inicia con bool para retornar valor booleano
   
    while (eslabon->pos_x > 0 || eslabon->pos_y > 0) { // Mientras la pos_x o pos_y sean mayor a 0 se ejecuta el ciclo
        if (eslabon->pos_x > 0) {
            eslabon->pos_x -= 1.0; // Si la posicion de x es mayor a cero se le resta 1.0
        }
       
        if (eslabon->pos_y > 0) {
            eslabon->pos_y -= 1.0; // Si la posicion de y es mayor a cero se le resta 1.0
        }
    }
   
    if (eslabon->pos_x <= 0 && eslabon->pos_y <= 0) { // Si las posiciones de pos_x y pos_y son menores o igual a 0 se sobreescribe el valor a 0 extacto (por si una resta deja algun valor negativo)
        eslabon->pos_x = 0;
        eslabon->pos_y = 0;
       
        return true;
    }
}

int main()
{
    srand(time(NULL)); // Inicializa semilla aleatoria
   
    // se definen estructuras declarando su id directamente
    struct Eslabon_brazo id1 = {1};
    struct Eslabon_brazo id2 = {2};
    struct Eslabon_brazo id3 = {3};
    struct Eslabon_brazo id4 = {4};
    
    // Se ejecutan funciones para posiciones iniciales
    pos_inicial(&id1.pos_x, &id1.pos_y);
    pos_inicial(&id2.pos_x, &id2.pos_y);
    pos_inicial(&id3.pos_x, &id3.pos_y);
    pos_inicial(&id4.pos_x, &id4.pos_y);
   
   
    // Se ejecutan funciones para auto-home con un if para que se muestre en pantalla cuando se termine de ejecutar la funcion
    if (auto_home(&id1)) {
        printf("Eslabon 1 terminado.\n");
    }
   
    if (auto_home(&id2)) {
        printf("Eslabon 2 terminado.\n");
    }
   
    if (auto_home(&id3)) {
        printf("Eslabon 3 terminado.\n");
    }
   
    if (auto_home(&id4)) {
        printf("Eslabon 4 terminado.\n");
    }
   
    printf("Todos los eslabones realizarion auto-home correctamente.");

    return 0;
}