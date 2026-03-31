# Parte 1

##Ejercicio 1 — Suma de números en lista, Crea una lista con al menos 8 números.
#Recorre la lista.
#Calcula la suma total.
#Muestra el resultado.

lista = [1,2,3,4,5,6,7,8]

suma = 0

for number in lista:
    suma = suma + number 
    print(suma)

## Ejercicio 2 — Contar mayores de edad, Crea una lista de edades.
#Recorre la lista.
#Cuenta cuántas personas son mayores o iguales a 18.
#Muestra el total.

edades = [12,20,40,5,14]

contador = 0

for age in edades:
    if age >= 18:
        contador = contador + 1
        print("mayor de edad")
    print(contador)

## Ejercicio 3 — Buscar elemento en lista, Crea una lista de nombres.
#Pide un nombre al usuario.
#Indica si el nombre está o no en la lista

names = ["Carlos", "Andrea", "Sandro", "Rafael", "Victoria", "Valeria"]

user = input("Hola, coloca tu nombre:")


if user in names:
      print("el nombre está en la lista")
else:
      print("no encontrado")
    

##Ejercicio 4 — Promedio de notas con lista, Crea una lista con 5 notas.
#Calcula el promedio usando un ciclo.
#Muestra el promedio final

notas = [10,20,3,4,15]

promedio = 0

for calculo in notas:
     promedio = promedio + calculo

     print(f"{promedio / 5: .2f}")

##Ejercicio 5 — Diccionario de productos, Crea un diccionario con productos y precios.
#Recorre el diccionario.
#Muestra cada producto con su precio

Productos = { 
     "producto": {"Pan", "DS", "Coca Cola"},
     "precio": {"20", "15", "300"}
}

print(f"productos: {Productos['producto']}, precios {Productos['precio']}")

##Ejercicio 6 — Suma de valores en diccionario, Crea un diccionario donde:
#La clave sea el nombre de un estudiante.
#El valor sea su nota.
#Recorre el diccionario.
#Calcula el promedio de todas las notas.

alumno = {"estudiante": "José Petit", "notas": [10,20,4,5]}

nota = alumno["notas"]

for promedio in alumno:
     promedio = sum(nota) / len(nota)

     print(f"el alumno {alumno["estudiante"]} tiene de promedio {promedio:.2f}")

if promedio >= 9.5:
     print("APROBÓ")
else:
     print("reprobó")

# PARTE 2:

##Ejercicio 7 - Contar ocurrencias
#Crea una lista con números repetidos. 
# Crea una función que reciba la lista y un número. 
# Valida y retorna cuántas veces está ese número en la lista.

repetidos = {1,1,5,5,2,2,3,3,50,52,50,52,4,4,5,15,15}

number = int(input("Hola querido usuario"))

def ocurrencias(lista,objetivo):
     contador = 0
     for n in lista:
          if n == objetivo:
               contador += 1 

resultado = ocurrencias (repetidos, number)

print(f"el numero {number} aparece {resultado} veces")                

##Ejercicio 8 - Inventario básico
#Crea un diccionario que represente un inventario (Producto → cantidad disponible). 
# Recorre el diccionario y muestra solo los productos cuya cantidad sea menor a 5.

inventario = [
    {"nombre": "Pan", "cantidad": 4},
    {"nombre":"Coca", "cantidad": 10},
    {"nombre":"Agua", "cantidad": 12}
]

for producto in inventario:
     print(f"{producto['nombre']}, {producto['cantidad']}")
     if producto['cantidad'] < 5:
          print(f"Alarma: {producto['nombre']} tiene poco stock {producto['cantidad']}")


##Ejercicio 9 - Lista de diccionarios
#Crea una lista donde cada elemento sea un diccionario con nombre y edad. 
# Crea una función que reciba la lista y la recorra, luego muestra con un print solo los nombres de las personas mayores de edad.

diccionarios = [    
     {"nombre": "Ana", "edad": 20}, 
     {"nombre": "Luis", "edad": 9},
     {"nombre": "Pedro", "edad": 18}
]

def mayor(lista):
     for persona in lista:
          if persona["edad"] >= 18:
               print(persona["nombre"])

mayor(diccionarios)


##Ejercicio 10 - Menú repetitivo con lista, Crea un menú que permita:

#Agregar un nombre a una lista.

#Mostrar todos los nombres.
#Salir.
#El menú debe repetirse hasta que el usuario elija salir.

name = []

while True:
     print("Opciones presentes")
     print("")
     print("1. Colocar nombre")
     print()
     print("2, Observar nombres dentro de la lista")
     print()
     print("3, Salir")

     print(f"Nombres que nadie recuerda ")
     opcion = int(input("Elige una opción (1,2,3):"))
     match opcion:
          case 1:
               name.append()
          case 2:
               for user in name:
                    print(user)
          case 3:
               print("Perfecto, muchas gracias")
               break
          case _:
               print("Opcion incorrecta, usted parece no haber situado las opciones anteriores")
               break 
