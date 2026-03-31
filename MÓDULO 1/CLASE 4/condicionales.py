#si =if (Condición):
#sino = else
# else = nunca tiene condición
# Bloque de código: Conjunto de líneas que se ejecutan juntas
# Identación: Espacios en blanco al inicio de una línea de código, que indican en que código de bloque pertenece la línea
# si elif (condición), cuando tengamos más de 2 condiciones
x= None

if x is None:
  print (True)
else:
  print (False)

edad = 19
if (edad >= 18):
   print (True)
else:
   print (False)

edad = int(input("Ingrese su edad:"))
sexo = input("Ingrese su sexo (M/F):")

# soy tu pensión >:)

if (sexo == "F" and edad >= 55):
   print ("hola")
elif (sexo == "M" and edad >= 60):
   print ("hola")
else:
   print ("tu que haces aquí")

total_compra = float(input("Ingrese su monto:"))
descuento1 = 10
descuento2= 20 

if (total_compra >= 500):
   descuento = total_compra * 0.1
   montofinal= total_compra - descuento
   print(f" el monto final es", montofinal)
elif (total_compra >= 1000):
   descuentof =  total_compra * 0.2
   montofinal2= total_compra - descuentof
   print(f"el monto final 2 es ", montofinal2)
else :
   print ("no")

# crear un programa que permita crear el acceso de un usuario al sistema
# dos constantes o variables fijas dentro del programa

