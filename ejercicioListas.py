# preguntale al usuario 5 numeros y luego imprime la suma de todos los numeros
#las listas son dinamicas en python


lista = []

numero = int(input("Ingresa un numero: "))

#.append es añadir el valor numero al final de la lista

lista.append(numero)
lista.remove(numero)

numero = int(input("Ingresa un numero: "))
lista.append(numero)


numero = int(input("Ingresa un numero: "))
lista.append(numero)

numero = int(input("Ingresa un numero: "))
lista.append(numero)


numero = int(input("Ingresa un numero: "))
lista.append(numero)

suma = lista[0] + lista[1] + lista[2] + lista[3] + lista[4]
suma2 = sum(lista)


print(suma)
print(suma2)



