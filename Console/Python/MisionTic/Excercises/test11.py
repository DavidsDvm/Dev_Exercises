"""
Condicional de notas escolares
"""

def notas():

    notadef = input("Ingrese su nota definitiva (Rango de 00 a 50): ")

    try:
        notadef = int(notadef)
    except ValueError:
        print ("No ingreso un valor valido!! solo se admiten numeros")
        notas()

    if notadef > 50 or notadef < 00 :
        print ("No ingreso un valor valido! (Solo numeros de 00 a 50)")
        notas()
    else:
        if notadef < 30:
            print ("Perdido la materia")
        elif notadef >= 30:
            print ("Paso la materia")
            if notadef >= 40:
                print ("Tiene buen promedio, felicidades")
        else:
            print ("No ingreso un valor valido!! solo se admiten numeros")
            notas()
notas()