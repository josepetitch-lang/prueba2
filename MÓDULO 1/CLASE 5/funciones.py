# snake_case 

def calculo():
    nota1= int(input("pon tu mierda:"))
    nota2= int(input("pon tu verga:"))
    nota3= int(input("dross te odia xd:"))
    notas= (nota1 + nota2 + nota3) / 3
    return(notas)
 
print(calculo())

def saludar_con_parametro(name):
    print("hola, bienvenido")
    print()
    print()
    print("Hola" + " "+ name + " " "bienvenido")

saludar_con_parametro("Luis")

usd_to_bs= 350
usd_to_eur= 0.94
def conversormoneda(par,monto, simbolo):
    print (par * monto, simbolo)

conversormoneda(usd_to_bs,100, "bs")


# Crea un programa que:
#1) Pida al usuario nombre
#2) Peso real del paquete (en número)
#3) Peso volumétrico del paquete (número)

#2 Determine peso facturable:
# Si el peso real es mayor que el volumétrico, usamos peso real
# Si no (usar volumétrico)

#3 Calcular costo total:

#4 Muestra una "factura" con:
# CLIENTE, PESO REAL Y VOLUMÉTRICO, PESO FACTURABLE, COSTO POR KG, TOTAL A PAGAR


