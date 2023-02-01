

# Este código calcula tu IMC
# Autor: Iñaki
# Fecha: 2021-09-15
# Versión: 1.0


# Importamos la librería math

import math 

print("Hola bienvenido \nEste programa calcula tu IMC")   # \n es para saltar la linea

# le preguntamos al usuario si masa  en kg cómo un decimal (float)

masa = float(input("Ingresa tu masa en kg: "))

# Le preguntamos al usuario su altura en metros (float)

altura = float(input("Por favor ingresa tu altura en metros: "))


# calculamos el IMC  con la formula masa/ altura**2

IMC = masa/altura**2  


#imprimimos el IMC 

print("Tu IMC es: ", IMC)

