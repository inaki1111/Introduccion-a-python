#Ejercicios de python Martes 7 de febrero



"""Ejercicio 1:

Dados dos números enteros, 
devuelve su producto solo si el producto es igual o 
menor que 1000, de lo contrario, devuelve su suma."""

#Implementa to código aqui:

def ejercicio1():
    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    multiplicacion = numero1 * numero2
    if multiplicacion <= 1000:
        print(numero1 * numero2)

    else:
        print(numero1 + numero2)    


#----------------------------------------------------------------------------------


"""Ejercicio 2

Escriba un programa 
para iterar los primeros 10 números y en cada iteración, 
imprima la suma del número actual y anterior.

Salida esperada
Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17
"""

#Escribe tu código aqui:

def ejercicio2():
    for i in range(10):
        if i == 0:
            print("Current Number", i, "Previous Number ", i, " Sum: ", i)
        else:
            print("Current Number", i, "Previous Number ", i-1, " Sum: ", i + i-1)
    
    
#------------------------------------------------------------------



"""Ejercicio 3
Comprobar si el primer y último número de una lista es el mismo"""

lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = [2,3,4,6,7,8,2]

#Implementa tu código aqui

def ejercicio3(lista):

    if lista[0] == lista[-1]:
        print("True")
    else:
        print("False")

#------------------------------------------------------------------


"""Ejercicio 4
Mostrar números divisibles por 5 de una lista
"""

lista = [10, 20, 33, 46, 55]

#Implementa tu código aqui

def ejercicio4(lista):
    
    for i in lista:
        if i % 5 == 0:
            print(i)


#------------------------------------------------------------------

#Validación de los ejercicios

ejercicio1()