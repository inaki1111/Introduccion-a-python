

# función con un menú de opciones 

# opción 1 que sea la calculadora de IMC

# opcion 2 multiplicar dos números

#opción 3 salir  -> break   else 



#----------------------------------------------------------------------
# Definición de funciones

def menu():
    print("Bienvenido al menú")
    print("1. Calculadora de IMC")
    print("2. Multiplicar dos números")
    print("3. Salir")
    opcion = int(input("Elija una opción: "))
    return opcion

def calculadoraIMC():
    
    print("Hola bienvenido \nEste programa calcula tu IMC")   # \n es para saltar la linea

    # le preguntamos al usuario si masa  en kg cómo un decimal (float)

    masa = float(input("Ingresa tu masa en kg: "))

    # Le preguntamos al usuario su altura en metros (float)

    altura = float(input("Por favor ingresa tu altura en metros: "))


    # calculamos el IMC  con la formula masa/ altura**2

    IMC = masa/altura**2  


    #imprimimos el IMC 

    print("Tu IMC es: ", IMC)

    # creamos una condición para saber si el usuario está en su peso ideal

    if IMC >= 18.5 and IMC < 24.9:
        print("Tu IMC es ", IMC, "Peso Normal")

    elif IMC <= 24.9 and IMC < 29.9:
        print("Tu IMC es ", IMC, "Sobre peso")

    elif IMC >= 29.9: 
        print("Tu IMC es ", IMC, "Obesidad")

    else: 
        print("Tu IMC es ", IMC, "Por debajo del peso")


def multiplicarNumeros():
    numero1 = int(input("Ingresa un número: "))
    numero2 = int(input("Ingresa otro número: "))
    print("El resultado de la multiplicación es: ", numero1 * numero2)

def salir():
    print("Gracias por usar el programa")
    

#----------------------------------------------------------------------

# Programa principal

while True:

    menu()
    opcion = menu()

    if opcion == 1:
        calculadoraIMC()
        
    elif opcion == 2:
        multiplicarNumeros()
    
    elif opcion == 3:
        salir()
        