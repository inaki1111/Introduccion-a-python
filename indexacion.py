#lista 

# la última posición de la lista es  longitud de la lista - 1
# la primera posición de la lista es 0
#        0  1  2  3  4  5  6  7  8  9
# [0] indice 
 
lista = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]

print(lista)
print(lista[0])

# lista de strings

lista = ["hola", "como", "estas"]

print(lista)


# lista de listas
# n lista    0          1           2
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista)
 #  [n lista][n elemento]
print(lista[0][0])


print(len(lista)) # longitud de la lista


# lista vacia

lista = []

# agregar elementos a una lista

lista.append(11) # agrega el elemento 11 al final de la lista


valor = input("Ingresa un valor: ")
lista.append(valor) # agrega el valor ingresado por el usuario al final de la lista

print(lista)
