"""
    Leer x, y, z pasarlos a booleanos y operar la ecuacion (x ^ y) v -z
    e imprima a que valor booleano corresponde cada valor
"""

x,y,z = input("Ingrese tres valores (entre ceros y unos) para saber su valor boleano: ").split()

x = bool(int(x))
y = bool(int(y))
z = bool(int(z))
operation = (x and y) or not z

print("Si X es {} si Y es {} si Z es {}, el resultado de la operacion es {}".format(x,y,z,operation))