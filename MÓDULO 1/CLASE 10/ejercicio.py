nombre = input("pon su nombre:")
cedula = input("y su cedula:")

with open("archivo.txt", "w") as archivo: 
    archivo.write(f"{nombre}, {cedula}")