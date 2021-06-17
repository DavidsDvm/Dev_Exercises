"""
Enunciado

Reto 4: Detectando copia en los exámenes de programación:

    Uno de los profesores de programación de la Universidad Sergio Arboleda
    está comenzando a perder su memoria. Hace algún tiempo, cuando comenzó
    a trabajar como docente, no únicamente conocía perfectamente todos los nombres
    y apellidos de sus estudiantes, sino que además contaba con una habilidad
    increíble para detectar copia en los exámenes de programación.
    Estaba tan seguro de sus capacidades que mientras los estudiantes
    se concentraban en analizar los problemas y diseñar algoritmos,
    él se sentaba en la última fila del salón a preparar futuras clases
    sin preocuparse por los intentos de algunos estudiantes por hacer trampa.

    La habilidad del profesor se basa en su memoria fotográfica.
    Cuando el profesor calificaba era capaz de recordar a la perfección si
    había visto un examen con las mismas respuestas o no, y si las encontraba
    acusaba siempre al segundo estudiante de copiar. Lamentablemente,
    durante los últimos meses su memoria fotográfica ya no funciona
    como antes y ahora solo recuerda algunos de los últimos exámenes que ha calificado.

    Debido a estas circunstancias,
    el profesor ha decidido solicitar su ayuda para construir un programa
    en Python que le permita comprobar si la perdida de su memoria fotográfica
    podría tener como consecuencia una disminución en la cantidad
    de copias que se detectan durante los exámenes.

"""

__autor__ = "David Vargas Monroy"
__version__ = 0.1

numeroExamenes, examenesRecuerda = input().split()
numeroExamenes = int(numeroExamenes)
examenesRecuerda = int(examenesRecuerda)
examenesRecuerda += 1
examenesCopiados = 0

n = str(input())
n = n.split(None,numeroExamenes)
Examenes = [int(i) for i in n]
numeroRepeticiones = len(Examenes) - len(set(Examenes))

for i in range(numeroExamenes):
    for c in range(1,examenesRecuerda):
        def calculo():
            operacion =  i - c
            if (operacion < 0):
                return None
            else:
                return Examenes[operacion]
        if (Examenes[i] == (calculo())):
            examenesCopiados += 1
            break
print(numeroRepeticiones,examenesCopiados)
