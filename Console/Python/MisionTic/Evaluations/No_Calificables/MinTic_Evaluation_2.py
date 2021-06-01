#=_Describcion del problema_=
"""
Enunciado:

    Manejo de tipos de datos en Python,Identifica el tipo de dato 
    (int, float, string o list) de los siguientes valores literales:
    Hola Mundo [1, 10, 100] -25 1.167 [Hola,Mundo] True A={Uno:uno, Dos:dos},
    Para la solución de este problema, se requiere que el usuario ingrese los
    datos y realice la validación del tipo de dato. Se requiere que se escriba
    el dato ingresado, se imprima por consola y luego se imprima qué tipo de dato es.

Dificultad:

    Baja

Instrucciones:

    Para la solución de este problema, se requiere que el usuario ingrese los datos
    y realice la validación del tipo de dato. Se requiere que se escriba el dato ingresado,
    se imprima por consola y luego se imprima qué tipo de dato es.
"""
#=_| Elaborado por : David Vargas Monroy | Grupo: 24 | Manejo de tipos de datos en Python |_=

from ast import literal_eval

input_data = input("Ingrese cualquier digito para conocer su tipo de dato: ")

def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str

print ("El tipo de dato del valor:",input_data,"Es de tipo:",get_type(input_data))