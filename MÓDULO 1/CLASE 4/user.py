number1 = int(input("Ingrese número 1:"))
number2 = int(input("Escriba el número 2:"))
number3 = int(input("¿Y el número 3?:"))
number4 = int(input("No hay numero 3 sin un numero 4, escribalo: "))

suma = number1 + number2 + number3 + number4
print(suma)
resta = number1 - number2 - number3 - number4
print(resta)
multiplicación = number1 * number2 * number3 * number4
print(multiplicación)
división = number1 / number2 / number3 / number4
print(división)

variable1 = suma
variable2 = multiplicación

print("La Variable 1 es:", variable1)
print("La Variable 2 es:", variable2)

print("es igual?:", variable1 == variable2)
print("V1 es mayor a V2", variable1 > variable2)
print("V1 es menor a V2", variable1 < variable2)
print("V1 es diferente a V2", variable1 != variable2)
print("V1 es mayor o igual que V2", variable1 >= variable2)
print("V1 es menor o igual que V2", variable1 <= variable2)

variable3 = resta
variable4 = división

print("La variable 3 es:", variable3)
print("La variable 4 es:", variable4)

print("es igual?:", variable3 == variable4)
print("V1 es mayor a V2", variable3 > variable4)
print("V1 es menor a V2", variable3 < variable4)
print("V1 es diferente a V2", variable3 != variable4)
print("V1 es mayor o igual que V2", variable3 >= variable4)
print("V1 es menor o igual que V2", variable3 <= variable4)

print ("si?", variable1 == 33)
print ("no?", variable2 != 33)
print ("quizas...", variable3 <= 33)
print ("eh...", variable4 >= 33)

# si ves esto, te deseo una infeliz noche >:)