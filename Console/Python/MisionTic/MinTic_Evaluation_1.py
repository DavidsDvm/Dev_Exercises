"""
    Enunciado:

Realiza un programa que cumpla con el siguiente algoritmo, utilizando siempre que sea posible,
operadores en asignación: Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Asignar a otra variable numero_usuario. Hay que especificar que sea entre 1 y 9 
(asegúrate que es un número) Multiplica el numero_usuario por 9 en sí mismo Multiplica
el numero_magico por el numero_usuario en sí mismo Finalmente muestra el valor final 
del numero_magico por pantalla

    Dificultad:

Media

    Instrucciones:

Para la solución de este problema, se requiere que el usuario ingrese un número entero
y el sistema realice el cálculo respectivo para hallar la multiplicación.
Para esto se debe usar la siguiente expresión. (multiplicación = numero_usuario X numero_magico).
Por último, realizar la impresión por pantalla de la multiplicación
"""

numero_magico = 12345679
numero_usuario = int(input("Ingresa un numero del 1 al 9: "))
if (numero_usuario >= 1 and numero_usuario<=9):
    numero_usuario *= 9
    numero_magico *= numero_usuario
    print(numero_magico)
else:
    print ("No se admiten numeros que no esten dentro del rango del 1 al 9")