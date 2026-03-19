#Ejercicio 2 – Descarga de un Banco de Baterías
Volatje_inicial = float(input("Ingrese el valor de voltaje "))
Voltaje_minimio = float(input("Ingrese el valor de voltaje minimo de operacion "))
Horas = 0
while Volatje_inicial > Voltaje_minimio:
    Volatje_inicial *= 0.97
    Horas += 1
print("El banco de baterias logro entregar energia durante ", int(Horas), "horas")
