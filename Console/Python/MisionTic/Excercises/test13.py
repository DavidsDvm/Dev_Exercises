"""
    Hacer un programa que lea un numero y que diga si es entero positivo o negativo
    y diga si es cero, negativo o positivo.
"""

def numblock():
    num = input("Ingrese un numero, para saber si es positivo o negativo: ")

    try:
        num = int(num)
    except:
        print("INGRESO un valor no valido, vuelva a intentar")
        print("~____________________________________________~")
        numblock()

    if num == 0:
        print("El numero es igual a CERO")
    elif num > 0:
        print("El numero es POSITIVO")
    elif num < 0:
        print("El numero es NEGATIVO")
    else:
        print("INGRESO un valor no valido, vuelva a intentar")
        print("~____________________________________________~")
        numblock()

numblock()
