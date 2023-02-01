# preguntale al usuario 5 numeros y luego imprime la suma de todos los numeros



lista = []

numero = int(input("Ingresa un numero: "))
lista.append(numero)


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



