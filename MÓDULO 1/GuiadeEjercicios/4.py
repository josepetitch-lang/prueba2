# Ejercicio 1:

numero= 100

while numero < 250:
    print(f"Número, {numero}:")
    numero += 1

# Ejercicio 2:

suma = 0

while True:
    num = int(input("Ingrese un número positivo o negativo [este ultimo por si desea irse]:"))

    suma += num

    if num < 0:
        print("Programa finalizado")
        break

# Ejercicio 3:

numbersecret = 5

np = int(input("¿PODRÁS ADIVINAR? COLOQUE SU NUMERO SECRETO:"))

while np != numbersecret:

    print("MAL, INTENTE DE NUEVO")

    np = int(input("¿PODRÁS ADIVINAR? COLOQUE SU NUMERO SECRETO:"))


    if np == numbersecret:
        print("FELICIDADES")
        break

# Ejercicio 4:

tabla = int(input("USTED.... ¿de qué numero desea ver su tabla?:"))

print(f"Tabla del {tabla}")

for i in range (1,11):
    resultado = tabla * i
    print(f"la tabla de {tabla} x {i} = {resultado}")

# Ejercicio 5:

pares = 0

for i in range(1,101):
    if i %2 == 0: 
        pares += 1

print(f"Hay entre 1, al 100. un total de {pares} números pares")
        
# Ejercicio 6: 

print("vamos desde 20 al 1... INICIANDO PROCESO")

for i in range(20,0,-1):
    print(f"vamos por el número {i}")