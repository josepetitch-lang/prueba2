# estructuras de datos

# Listas
# Tuplas
# Diccionarios 

# Listas: permite almacenar datos de forma ordenada y de facil acceso

machete = ["Machete", "Machete", "Machete"]

numeros = [1,3,4]

bool= [True, False]

webon = ["José", 18, "32569485", [12,20]]

# Indíce: cada elemento tiene un indice q va de 0 a n, ejemplo: print(numeros[1])

numeros[2]= 55

print(numeros[1], numeros [2])

numeros.append(5)

print(numeros)

numeros.reverse()

print(numeros)

numeros.insert(1, 30)
print(numeros)

import random

num= random.sample(numeros,4)

print(num)

i= 0
while i < len(numeros) :
    print(f"numero {i + 1} es el {numeros[i]}")
    
    i += 1

for numero in numeros:
    print(f"el numero es {numero}, y su indice es {numeros.index(numero)}")




 