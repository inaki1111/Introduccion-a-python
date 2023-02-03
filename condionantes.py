
# preguntar a la maquina algo 

 #  = ES ASIGNACIÓN
    # == ES COMPARACIÓN

# comparadores logicos
# == igual
# != diferente
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que



numero1 = 3
numero2 = 1

if numero1 == numero2:
    print("son iguales")

elif numero1 > numero2:
    print("numero1 es mayor")  

elif numero1 < numero2:
    print("numero2 es mayor")

else:
    print("no son iguales")


#  and las dos condiciones deben ser verdaderas
#  or una de las condiciones debe ser verdadera


numero1 = 1
numero2 = 2
numero3 = 2

if numero1 == numero2 or numero1 == numero3:
    print("son iguales")

elif numero1 > numero2:
    print("numero1 es mayor")