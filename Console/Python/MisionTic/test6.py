"""
Calcular nota definitiva ciclo 1 la cual se divide en:
5 retos y nota de ingles
reto 1: 10%
reto 2: 10%
reto 3: 20%
reto 4: 20%
reto 5: 20%
Curso de ingles: 20%
"""

print ("~=======================================~")
nota1 = int(input("Ingrese la nota #1: "))
print ("~=======================================~")
nota2 = int(input("Ingrese la nota #2: "))
print ("~=======================================~")
nota3 = int(input("Ingrese la nota #3: "))
print ("~=======================================~")
nota4 = int(input("Ingrese la nota #4: "))
print ("~=======================================~")
nota5 = int(input("Ingrese la nota #5: "))
print ("~=======================================~")
ing = int(input("Ingrese la nota de ingles: "))
print ("~=======================================~")

nota1 *= 0.1
nota2 *= 0.1
nota3 *= 0.2
nota4 *= 0.2
nota5 *= 0.2
ing *= 0.20

total = int(nota1+nota2+nota3+nota4+nota5+ing)

print ("La nota definitiva del su ciclo 1 es igual a:",total)
