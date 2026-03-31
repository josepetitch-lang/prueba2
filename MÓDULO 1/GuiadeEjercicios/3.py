# Ejercicio 1: Escribe un programa que pida un número al usuario e indique si el número es: +. -. 0

number = float(input("Coloque un número:"))

if number < 0:
    print("Este número es negativo")
elif number > 0:
    print("Este número es positivo")
else:
    print("no si muy alto, es cero")

# Ejercicio 2: Desarrolla un programa que pida una cantidad en $ y transforma a bs usando tasa fija

dolar_to_bs= 360

def conversormoneda():
    dolar = int(input("Monto total en dolares:"))
    print(dolar_to_bs * dolar)

conversormoneda()

# Ejercicio 3: Pide un usuario un número del 1 al 7 que represente un día de la semana

day= int(input("Coloque un número dentro del 1 al 7: "))

if day >= 1 and day <= 5: 
   print("Día laboral JAJAJAJAJAJA ")
elif day == 6 or day == 7:
    print("Fin de semana...")
else:
    print("?")

# Ejercicio 4: pide dos números al usuario y muestra en pantalla los resultados

numero1= float(input("Ingrese el primer número: "))
numero2= float(input("Ingrese el segundo número: "))
operator= input("Ingrese la operación a realizar (+,-,*):")

def calcular (numero1, numero2, operator):
    operator =print("Seleccione una acción entre (+,-,*):")
    if operator == "+":
        return numero1 + numero2
    elif operator == "-":
        return numero1 - numero2
    elif operator == "*":
        return numero1 * numero2
    else:
        return "nope, ingrese una de las 3 acciones correctas"
    
resultado = calcular(numero1,numero2, operator)

print(resultado) 

# Ejercicio 5: Crea un sistema de acceso básico que pida una contraseña

contraseña = input("Escribe tu contraseña:")

if contraseña == "python123":
    print("ACceso Permitido")
else:
    print("Acceso Denegado, intente nuevamente")

# Ejercicio 6: Define una función que recibe el radio de un circulo, retorne su área 

radio = int(input("indique el radio del circulo:"))

area = 3.141592 * (radio ** 2)

print("El area del circulo es", area)

# Ejercicio 7: Crea una función que reciba una temperatura en C° y lo retorne en Fahreinheit 

C = int(input("Coloque por favor el C°: "))

F = (C * 1.8) + 32

print("El resultado en F° es", F)

# Ejercicio 8: Crea una función que reciba una edad y retorne un valor booleano

edad= int(input("Escriba su edad:"))

if edad >= 18:
    print (True)
else:
    print (False)

# Ejercicio 9: Pide 3 numeros al usuario, calcula el promedio y muestralo en pantalla

n1 = int(input("Escriba el número:"))
n2 = int(input("Escriba el número:"))
n3 = int(input("Escriba el número:"))

def promedio():
    suma = n1 + n2 + n3
    print(suma/3)

promedio()

# Ejercicio 10: Crea un programa para calcular el salario de un empleado

horaschamba = float(input("Diga sus horas de trabajo:"))
pago_por_hora = float(input("SU pago por hora es?:"))

salario = horaschamba * pago_por_hora

print("Su salario es", salario)

# Ejercicio 11: Pide edad y nombre del usuario

name= input("Escriba tu nombre:")
age = int(input("Escribe tu edad:"))

if age < 18:
    print("Hola pequeño...", name)
else:
    print("Hola estimado", name)

# Ejercicio 12: Pide una temperatura en C° e indica el clima:

temperatura= float(input("Indica la temperatura en C°:"))

if temperatura < 15:
    print("Frio")
elif temperatura == 15 and temperatura <= 25:
    print("Templado")
else:
    print("Calor")
