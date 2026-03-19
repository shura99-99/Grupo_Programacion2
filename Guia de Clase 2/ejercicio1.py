# Lista de voltajes medidos durante la descarga de una batería
#voltajes = [12.6, 12.4, 12.3, 12.1, 11.9, 11.8, 11.6, 11.4]

import random
voltajes = [round(random.uniform(10.0, 12.0), 1) for _ in range(10)]
#lista = [round(random.uniform(inicio, final), cant_de_decimales) for _ in range(cant_de_numero)]

def analizar_voltajes(lista_voltajes):
    """
    Esta función recibe una lista de voltajes y calcula:
    - voltaje máximo
    - voltaje mínimo
    - voltaje promedio
    - cantidad de mediciones bajo 12.0 V
    """

    # Suponemos que el primer valor es inicialmente el máximo y el mínimo
    maximo = lista_voltajes[0]
    minimo = lista_voltajes[0]

    suma = 0
    cantidad_bajo_12 = 0

    # Recorremos toda la lista
    for voltaje in lista_voltajes:
        suma += voltaje

        # Verificamos si es mayor que el máximo actual
        if voltaje > maximo:
            maximo = voltaje

        # Verificamos si es menor que el mínimo actual
        if voltaje < minimo:
            minimo = voltaje

        # Contamos cuántas mediciones están bajo 12.0 V
        if voltaje < 12.0:
            cantidad_bajo_12 += 1

    # Calculamos el promedio
    promedio = suma / len(lista_voltajes)

    # Retornamos todos los resultados
    return maximo, minimo, promedio, cantidad_bajo_12


def estado_bateria(promedio):
    """
    Esta función clasifica el estado de la batería
    según el voltaje promedio.
    """
    if promedio >= 12.2:
        return "Batería en buen estado"
    elif promedio >= 11.8:
        return "Batería en descarga"
    else:
        return "Batería crítica"


# Llamamos a la función principal de análisis
v_max, v_min, v_prom, bajo_12 = analizar_voltajes(voltajes)

# Determinamos el estado de la batería
estado = estado_bateria(v_prom)

# Mostramos los resultados
print("=== Análisis de Voltajes ===")
print("Voltajes: ", voltajes)
print(f"Voltaje máximo: {v_max} V")
print(f"Voltaje mínimo: {v_min} V")
print(f"Voltaje promedio: {v_prom:.2f} V")
print(f"Cantidad de mediciones bajo 12.0 V: {bajo_12}")
print(f"Estado de la batería: {estado}")
