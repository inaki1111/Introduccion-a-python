# trabajar con listas 
# importar libreria numpy

import numpy as np

# crear una lista

lista = np.array([1,2,3,4,5])


print(type(lista))

print(lista)



# crear listas de una dimensión 

arr = np.array([42,3])

print(arr)


# listas de dos dimensiones


arr = np.array([[1,2], [3,5]])

print(arr)



#lista de 3 dimensiones

print("lista de 3 dimensiones")
arr = np.array([[[1,2,3], [4,5,6]],[[1,2,3], [4,5,6]]])

print(arr)


print("dimensiones ", arr.ndim)