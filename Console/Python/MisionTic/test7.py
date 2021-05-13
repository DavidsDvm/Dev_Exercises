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

print ("A continuacion se le permitira ingresar sus notas: ")
print ("Donde de la 1 a la 5 son el resultado de los retos y la 6 es la nota de ingles")

x=[]
total = 0

for i in range(6):	
    print ("~=======================================~")				
    x.append(input(f"Introduce tu nota #{i+1}: "))
    x[i] = int(x[i])
    if i < 2:
        x[i] *= 0.1
    elif i >= 2:
        x[i] *= 0.2    
    total += x[i]
    
print("Su nota definitiva fue de:",int(total))		