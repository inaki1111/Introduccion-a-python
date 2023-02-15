

# install the python package: pip install tk

import tkinter as tk
from tkinter import ttk


def mult():
    num1 = float(numero1.get())
    num2 = float(numero2.get())
    resultado = num1 * num2
    etiqueta3 = ttk.Label(text=resultado)
    etiqueta3.place(x=100, y=100, width=200, height=100)
    print(resultado)

# create the window

window = tk.Tk()
# set the title 
window.title("Programa 1")
# set the size
window.geometry("500x500")
# set the background color
window.configure(background="grey")

# crear una etiqueta 

etiqueta1 = ttk.Label(text="Multiplicacion de dos numeros")
etiqueta1.place(x = 100, y = 200, width=500, height=50)

etiqueta2 = ttk.Label(text="Tu resultado es: ")
etiqueta2.place(x = 100, y = 300, width=500, height=50)



numero1 = ttk.Entry()
numero1.place(x = 100, y = 400, width=500, height=50)

numero2 = ttk.Entry()
numero2.place(x = 100, y = 500, width=500, height=50)


boton_multiplicar = ttk.Button(text="Multiplicar", command=mult)
boton_multiplicar.place(x = 100, y = 600, width=500, height=50)


window.mainloop()
