# Archivos en python: nos permite leer y escribir archivos, para persistir datos

# Abrir archivos: #open('nombre_archivo', 'modo') -> 'r' (read [leer]), 'w'(write [leer]) ´a´ (append [aparece]) pip


archivo = open('archivo.txt', 'a')

archivo.write("soy Jose :3")
archivo.write ("Hola")

archivo.close()

