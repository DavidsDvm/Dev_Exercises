"""
    Utilizacion de un while para hacer una suma hasta llegar a un numero
"""
n = int(input("Ingrese un numero: "))
suma = 0
suma += n

if suma == 0:
    print("Ingreso un valor no valido")
else:
    while suma < 100:
        print("Aun la suma no llega a 100, el total por ahora es:{}".format(suma))
        n = int(input("Ingrese otro numero para sumar: "))
        suma += n
