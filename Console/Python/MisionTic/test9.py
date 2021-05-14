"""
Ingresa unos grados en Celcius y se transforman a lo que el usuario desee, ya sea Kelvin o Farenheit
"""
def conver():
    print ("Recuerda [(Grados) (TIPO: k o f)]")
    grados,tipo = input("Ingresa los grados que tienes y el tipo de dato al que quieres hacer la conversion: ").split()

    grados = int(grados)

    if tipo == 'f' or tipo == 'F':
        resultado = grados * 1.8000 + 32
        print ("Su resultado es igual a:",resultado,"grados Farenheit")
    elif tipo == 'k' or tipo =='K':
        resultado = grados + 273.15
        print ("Su resultado es igual a:",resultado,"grados Kelvin")
    else:
        print("Ingreso un caracter no valido!!")
        print("Vuelva a intentarlo")
        print ("~=========================================================~")
        conver()
conver()