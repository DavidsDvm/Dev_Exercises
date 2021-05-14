"""
Creation of conditionals where we found if a number is even or odd
"""

num = int(input("Ingrese un numero para saber si es par o impar: "))

num %= 2

if num == 0:
    print("El numero es PAR")
else:
    print("El numero es IMPAR")