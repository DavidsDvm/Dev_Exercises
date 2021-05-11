numero_magico = 12345679
numero_usuario = int(input("Ingresa un numero del 1 al 9: "))
if (numero_usuario >= 1 and numero_usuario<=9):
    numero_usuario *= 9
    numero_magico *= numero_usuario
    print(numero_magico)
else:
    print ("No se admiten numeros que no esten dentro del rango del 1 al 9")