#Ejercicio 2:
name = input("sup, dame tu nombre:")
numero1 = int(input("Coloque el número:"))
numero2 = int(input("Indique el segundo valor:"))
numero3 = int(input("Coloque su número:"))

if (numero1 > numero2 and numero1 > numero3):
    print("El mayor es", numero1)
elif (numero2 > numero1 and numero2 > numero3 ):
    print("El valor mayor es", numero2)
else:
    print("El mayor es: ", numero3)
    
# Ejercicio 3:
peso =  float(input("Cual es su peso (en kg?):"))

if peso <= 5:
    print("cuesta 5")
elif peso > 5:
    print("Cuesta 10")

# Ejercicio 4:

minutos = int(input("Cuantos minutos han transcurrido?"))

seg = minutos * 60
hora = minutos/60
minutos = minutos - (hora * 60)

print("Han transcurrido", hora , "horas" , minutos , "minutos" , "y" , seg , "segundos")





