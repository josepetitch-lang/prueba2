# EJERCICIO 1: control de aforo :p
# un local tiene un limite de 20 personas, simulemos el ingreso de personas 
# mostramos en pantalla los que van ingresando, contamos hasta 20 (indicamos en 20, "aforo completo")


# cuantas personas han llegado?, sumamos, hasta q llegue a 20 

# EJERCICIO 2: Revisión de pedidos
#pedimos un numero al usuario de pedidos, y por cada pedido, vamos a indicar "revisado pedido hasta todos los pedidos totales"


#R1: 

ntotal = 20

contador = 0

while contador <= ntotal :
      n= int(input("cuantas personas han llegado:"))
      contador += n
      if contador >= ntotal:
            print("aforo lleno")
            break

# R2: pen
