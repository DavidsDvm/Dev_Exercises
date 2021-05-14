"""
Indicar que significa un color de semaforo
"""

def semaforo():
    c = input ("Ingrese en que color se encuentra el semaforo: ")

    if c.lower() == "rojo":
        print ("Significa pare")
    elif c.lower() == "amarillo":
        print ("Significa precaucion")
    elif c.lower() == "verde":
        print ("Significa siga")
    else:
        print ("Usted no indico un valor dentro de los limites")
        print ("~===============================~")
        semaforo()
semaforo()