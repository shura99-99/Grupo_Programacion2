# Ejercicio 3 - Menú de Conversión de Unidades
while True:
    print("1. Convertir miliamperios (mA) a amperios (A)")
    print("2. Convertir microfaradios (uF) a faradios (F)")
    print("3. Convertir kiloohmios (kOhm) a ohmios (Ohm)")
    print("4. Salir")
    opcion = int(input("Digite el numero de la opcion de desee: "))
    if opcion == 1:
        mA = float(input("Ingrese el valor en mA: "))
        print((mA),"mA equivalen a ", (mA/1000),"A")
    elif opcion == 2:
        uF = float(input("Ingrese el valor en uF: "))
        print((uF),"uF equivalen a ", (uF/1000000),"F" )
    elif opcion == 3:
        K_Ohms = float(input("Ingrese el valor en KOhms: "))
        print((K_Ohms),"KOhms equivalen a ", (K_Ohms*1000), "Ohms")
    elif opcion == 4:
        print("Finalizando...")
        break
    else:
        print("Error, opcion no valida. Digite el numero de la opcion de desee: ")
