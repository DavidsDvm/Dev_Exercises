"""
    Creacion de factorial de un numero
"""

num = 1

n = int(input("Digite el numero que quiere convertir en factorial: "))

for i in range(1, n+1):
    num *= i
if n == 0 or n == 1:
    num = 1
print("El factorial de {} es igual a {}".format(n, num))