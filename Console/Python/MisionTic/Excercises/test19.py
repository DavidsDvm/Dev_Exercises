"""
    Creacion de un contador que cuente los multiplos de 6 hasta 100
"""

num = 0

for i in range(6, 100, 6):
    num += 1
    print("El multiplo es: {} Y van {} en total".format(i,num))
print ("hay",num,"Multiplos de 6 hasta 100")