"""
    Hacer un programa que lea un valor entero correspondiente a la edad
    en donde mire si es mayor, menor o tercera edad
"""

def numblock():
    edad = input("Ingrese un numero, para saber si es usted en que rango de edad esta: ")

    try:
        edad = int(edad)
    except ValueError:
        print("INGRESO un valor no valido, vuelva a intentar")
        print("~____________________________________________~")
        numblock()

    if edad < 0:
        print("ERROR no puede tener edad negativa, vuelva a intentar")
        print("~____________________________________________~")
        numblock()
    elif edad >= 0 and edad < 18:
        print("Usted es MENOR de edad")
    elif edad >= 18:
        print("Usted es MAYOR de edad")
        if edad > 60:
            print("Usted se encuentra en la tercera edad")
    else:
        print("INGRESO un valor no valido, vuelva a intentar")
        print("~____________________________________________~")
        numblock()

numblock()
