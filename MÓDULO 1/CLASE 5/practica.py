name = input("sup bro, what is ur name:")
pesoreal = float(input("Oye... eh, cual es el pesoreal?:"))
pesovolumétrico = float(input("cual es el peso volumétrico?:"))

costo_por_kg= 5

def costo_por_enviar (pesoreal, pesovolumétrico):
     if pesoreal > pesovolumétrico:
        pesofactura = pesoreal
     else:
        pesofactura= pesovolumétrico
     return pesofactura * costo_por_kg

print()
print("Factura:")
print()

costo_enviar = costo_por_enviar(pesoreal, pesovolumétrico)

def factura(name, pesoreal, pesovolumétrico, costo_por_kg, costo_enviar):
    print("Cliente:", name)
    print("Pesoreal:", pesoreal)
    print("Peso volumétrico", pesovolumétrico)
    print("costo por kg:", costo_por_kg)
    print("costototal:", costo_enviar)

factura(name, pesoreal, pesovolumétrico, costo_por_kg, costo_enviar)


