import math

def funcsen(x, amplitud, frecuencia, desfase):
    return amplitud * math.sin(frecuencia * x + desfase)

amplitud = 1.0
frecuencia = 1.0
desfase = 0.0

# Loop through x values from 0 to 10 in steps of 0.1
for x in range(0, 100, 1):
    x = x / 10.0
    value = funcsen(x, amplitud, frecuencia, desfase)
    print(value)
