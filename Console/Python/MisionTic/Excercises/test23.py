"""
    Escribe una funcion que reciba como parametro una cadena y devuelva un diccionario con
    la cantidad de apariciones de cada caracter en la cadena
"""

from typing import Collection


def count_array(cantidad):
    for c in cantidad:
        if c in cantidad:
            diccionario.update({c:cantidad.count(c)})

caracteres = input("Ingrese una cadena de texto: ")
diccionario = {}
count_array(caracteres)

print(diccionario)