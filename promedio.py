def calcularPromedio5(lista):
    promedio = (lista[0] + lista[1] +  lista[2] + lista[3] + lista[4])/5
    return promedio

# que me diga que promedio es mayor de dos listas 

lista1=[1,2,3,4,5]
lista2= [2,3,4,6,7]


promedio1 = calcularPromedio5(lista1)
promedio2 = calcularPromedio5(lista2)

if promedio1 > promedio2:
    print("promedio 1 es mayor  que promedio 2")

else:
    print("promedio 2 es mayor  que promedio 1")
