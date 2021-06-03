"""
    Creacion de ciclos while para hacer comparaciones
    y repetir iteraciones
"""

n = int(input("Digite un numero entero: "))
while n >= 0 and n <=20:
    print("el numero esta entre el rango de 0 y 20")
    n = int(input("El numero es {} escriba otro numero: ".format(n)))
    if n >= 20:
        print("el numero es mayor que 20")
