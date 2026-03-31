# Cicloa, Bucles, Loops
supercontador = 0
n= int(input("ponga su numero:"))

while n < 100:
    if n %2 == 0:
        print("es par, invitado de lamine yamal")
    else:
        print("es impar, mi cornudo")

    n += 1

n= int(input("ponga su numero:"))
nfin= int(input("ponga el ultimo numero:"))

mem = n

suma = 0

while mem <= nfin:
       suma += mem
       mem  += 1

print (f"La suma de todos los numeros de {n} a {nfin} es: {suma}")

