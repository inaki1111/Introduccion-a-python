import pandas

dataset = {
    "coches" : ["BMW", "VOLVO", "FORD"],
    "CALIICACIONES" : [1,2,3]
    }

myvar = pandas.DataFrame(dataset)

print(myvar)