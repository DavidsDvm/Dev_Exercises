"""
Una juguetería tiene mucho éxito en dos de sus productos:
payasos y muñecas. Suele hacer venta por correo y la empresa de logística
les cobra por peso de cada paquete así que deben calcular el peso de los payasos
y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada
muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas
vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""

print ("~===============================~")
print ("Bievenido a nuestro programa")
print ("~===============================~")
print ("Vamos a pedirte algunos datos a  continuacion: ")

clown = int(input("Digita la cantidad de payasos de juguete a enviar: "))
wrist = int(input("Digita la cantidad de munecas de juguete a enviar: "))

clown *= 112
wrist *= 75

total = clown + wrist

print ("~===============================~")

print ("El peso total del pedido es igual a: ",total," gramos")