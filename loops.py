# loops 

# whle loop mientras una variable sea verdadera se ejecuta el loop
# for loop se ejecuta un numero determinado de veces

# while loop

"""
numero = 1
contador = 10

while contador > 0:
    print(numero)
    numero = numero + 1 
    contador = contador - 1

"""
#Has un while loop que le pregunte al usuario que añada numeros a un lista hasta que el usuario diga que ya no quiere añadir mas numeros.

#.append() # añade un elemento al final de la lista
#print(lista) # imprime en pantalla


print("Ingresa numeros a la lista, si ya no quieres numero pon -1")
lista = []
numero = float(input("Ingresa un numero: "))
while numero != -1:
    lista.append(numero)
    numero = float(input("Ingresa un numero: "))

print(lista)

