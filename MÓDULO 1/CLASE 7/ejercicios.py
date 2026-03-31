# Ejercicio 1:

edades = [12,23,19,40,33,2]

for edad in edades:
    if edad >= 18:
        print(edad)

# Ejercicio 2:

numero = [10,20,30,40,50]

suma= 0

for calculo in numero:
    suma += calculo

print(f"La suma total de todos esos números es... {suma} :D")

   
numeros = [10, 11, 12, 40, 60]
suma_total = 0

i=0
while i < len(numeros):
    suma_total += numeros[i]
    i+=1 
    print(f"la suma total es {suma_total}")