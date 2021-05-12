"""
Una panadería vende barras de pan a 3.49€ cada una.
El pan que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número
de barras vendidas que no son del día.
Después el programa debe mostrar el precio habitual de una barra de pan,
el descuento que se le hace por no ser fresca y el coste final total.
"""

nPrice = 3.49

print ("~===============================~")
print ("Bievenido a nuestro programa")
print ("~===============================~")

bread = int(input("Digite la cantidad de barras de pan vendidas que no son del dia: "))

print ("El precio habitual del pan es de: ",nPrice,"€")
print ("~===============================~")
nPrice = nPrice - (nPrice * 0.6)
print ("El descuento que se le hace por pan es del: ",nPrice,"€")
print ("~===============================~")
nPrice = nPrice*bread 
print ("El coste total de los",bread,"panes es de: ",nPrice)