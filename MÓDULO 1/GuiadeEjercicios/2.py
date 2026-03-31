# Ejercicio 1: "Saludo Personalizado" (Pide el nombre del usuario y muestra un saludo personalizado)

nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")

username= nombre + " " +  apellido

print(f"hola," + " " + username + " " +", bienvenido :D")

# Ejercicio 2: "Suma de dos números" (Pide dos números al usuaeio y muestra la suma de ambos)

num1= int(input("Ingrese numero 1:"))
num2= int(input("Y el numero 2, o te lo comiste?:"))

sumatoria = num1 + num2
print("sumatoria total:", sumatoria)

# Ejercicio 3: Area de un rectángulo (Pide el alto y ancho de un rectángulo y muestra el área)

ancho = int(input("Ingrese cantidad total de cm del ancho:"))
alto = int(input("A su vez, el ancho: "))

area = ancho * alto

print("Hola" + " "+ username + " " + "el área total es" +" ", area)

# Ejercicio 4: Conversión de temperatura (Pide una temperatura en grados C° y transformala en F°)

GradosC = int(input("Coloque por favor el C°: "))

GradosF = (GradosC * 1.8) + 32

print("El resultado en F° es", GradosF)

# Ejercicio 5: Mayor o menor de edad

print("Buenas, querido usuario, le pido que rellene el siguiente dato")
userage = int(input("INGRESE SU EDAD:"))

if userage >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# Ejercicio 6: Número positivo, negativo o cero (Pide un número e indica si es positivo, negativo o cero)

numero= int(input("Ingrese el numero correspodiente:"))

if numero > 0:
    print("Es positivo (+)")
elif numero < 0:
    print("Es negativo (-)")
else:
    print("0")

# Ejercicio 7: Par o Impar (Pide un número e indica si es par o impar)

number = int(input(f"Hola"+ username + "escribe un numero aleatorio : "))

if number %2 == 0: 
    print("Es par")
else:
    print("Es impar")

# Ejercicio 8: Promedio de 6 notas (Pide 6 notas y muestra el promedio)

note_1 = int(input("Ingrese nota 1:"))
note_2 = int(input("Ingrese nota 2:"))
note_3 = int(input("Ingrese nota 3:"))
note_4 = int(input("Ingrese nota 4:"))
note_5 = int(input("Ingrese nota 5:"))
note_6 = int(input("Ingrese nota 6:"))

total_notas= (note_1 + note_2 + note_3 + note_4 + note_5 + note_6 / 6)

if total_notas >= 10:
    print("Aprobado")
else:
    print("Reprobado")

# Ejercicio 9: Descuento en una compra (Pide monto de una compra, si monto >= 100, descuento 10%)

monto= int(input("Ingrese el monto:"))

if monto >= 100:
   descuento = monto * 0.1
   montofinal= monto - descuento
   print(f" el monto final es", montofinal)
else:
    print(f"Su monto total es", monto)

# Ejercicio 10: Comparación de 2 números (Pide dos números y muestra cual es mayor o si son iguales)

N1= int(input("Ingrese el primer número:"))
N2= int(input("Ingrese el segundo número:"))

if N1 == N2: 
    print("son iguales")
elif N1 >= N2:
    print("1° es mayor que 2°")
else:
    print("2° es mayor que 1")

# Ejercicio 11: Calculo de salario

horas= int(input("Ingrese las horas de trabajo:"))
pago_hora= int(input("Ingrese el pago por hora que usted debe de recibir :"))

salario = horas * pago_hora

if salario >= 1000:
    print("Su salario es", salario, "Salario alto")
else:
    print("Su salario es:", salario)

# Ejercicio 12: Conversión de moneda (Pide una cantidad en $ y convertir a Bs. usando tasa fija)

dolares = int(input("Cuantos $ tiene usted?:"))

bolivares = dolares * 321.03

print("Su tasa en bolivares de ese total de $ es:", dolares)

# Ejercicio 13: Calculo de IMC:

peso= int(input("coloque su peso (kg):"))
estatura = float(input("coloque su estatura (m):"))

IMC = peso / estatura ** 2

print(IMC)

# Ejercicio 14: Validación de acceso:

usuario = int(input("Escriba el nombre:"))
contraseña = int(input("Escriba la contraseña:"))

if usuario == "admin" and contraseña == "1234":
    print("Acceso concedido")
else:
    print("Acceso denegado")

# Ejercicio 15: Evaluación de un número dentro de un rango:

numerito= int(input("COLOQUE SU NUMERO:"))

if 1 <= numerito <= 10:
    print("mas simple imposible, dentro de rango")
else:
    print("fuera bro, fuera")