"""
    Creacion de una interface grefica con tkinter
"""
from tkinter import *

def mostrarTexto():
    # texto hola mundo
    textoLabel2 = Label(window, text="Le diste click al botton", width=12)
    textoLabel2.grid(row=0,column=2)

def display():
    name = textVar.get()
    textoLabel.configure(text="Hola "+name)

window = Tk()

# texto hola mundo
textoLabel = Label(window, text="Hola mundo")
textoLabel.grid(row=0,column=1)

#Crea un input
textVar = StringVar("")
cajaTexto = Entry(window, textvariable=textVar, width=12)
cajaTexto.grid(row=1,column=0)

#Crear botton de salir
quitButton = Button(window, text = "Salir", command = window.destroy)
quitButton.grid(row=2,column=0)
#Crear botton para mostrar texto invisible
quitButton = Button(window, text = "Mostrar texto oculto", command = mostrarTexto)
quitButton.grid(row=2,column=1)
#Crear botton para saludar con nombre
quitButton = Button(window, text = "Dale para saludarte", command = display)
quitButton.grid(row=2,column=2)

mainloop()