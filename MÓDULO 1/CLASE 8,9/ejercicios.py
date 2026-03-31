# Ejercicio: Una lista de productos, tener un identificador para cada producto, un nombre y un precio 

frutas = [
    {"Identificador": "o2S3", "Fruta": "Pera", "Precio": 12 },
    {"Identificador": "P3I4", "Fruta": "Mango", "Precio": 5 },
    {"Identificador": "M3L2", "Fruta": "Manzana", "Precio": 20 }
]
    
# funcion calcular precio con IVA DE UN producto 

IVA = 0.16

def calcular_con_iva(precio):
     return precio * IVA 

# recorrer la lista de productos y a cada producto le agregamos un nuevo campo, 

for producto in frutas: 
     print(f"{producto['Fruta']}: {producto['Precio']}")

for producto in frutas:
     precio_with_iva = calcular_con_iva(producto['Precio'])
     print(f"{producto['Precio']}, {precio_with_iva:}")
     
print(frutas)

