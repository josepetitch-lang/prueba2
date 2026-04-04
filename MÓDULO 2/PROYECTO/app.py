import time
import models.usuario
from utils.json_manager import JsonManager

adm_libros = JsonManager("libros")
adm_users = JsonManager("usuarios")

datos_libros = adm_libros.read_json()
datos_usuarios = adm_users.read_json()

if __name__ == "__main__": 
    def menu():
        while True:
                print("1. Pedir")
                print()
                print("2. Entregar")
                print()
                print("3. Lista de Libros")
                print()
                print("4. Salir")
                print()
                opcion = input("Seleccione una de las opciones: ")

                if opcion == "1":
                    if sesion["tipo"] == "Professor":
                        user = models.usuario.Profesor(sesion["nombre"], sesion["cedula"], sesion["edad"], sesion["telefono"], sesion["gmail"], sesion["libros_prestados"])
                    else:
                        user = models.usuario.Estudiante(sesion["nombre"], sesion["cedula"], sesion["edad"], sesion["telefono"], sesion["gmail"], sesion["libros_prestados"])
                    
                    if user.puede_pedir():
                        libro_buscado = input("Nombre del libro que desea: ").lower()
                        encontrado = False 
                        
                        for libro_data in datos_libros:
                            if libro_data["titulo"].lower() == libro_buscado and libro_data["disponibilidad"]:
                                libro_data["disponibilidad"] = False
                                sesion["libros_prestados"].append(libro_data["titulo"])
                                
                                adm_libros.write_json(datos_libros)
                                adm_users.write_json(datos_usuarios)
                                print(f"FELICIDADES, LOGRÓ EL PRESTAMO: {libro_data['titulo']}")
                                encontrado = True
                                break
                        
                        if not encontrado:
                            print("El libro es como tu papá, no existe :D")
                    else:
                        print(f"Límite alcanzado para {sesion['tipo']}.")

                elif opcion == "2":
                    titulo_devolver = input("Ingrese el titulo del libro a devolver: ")
                    if titulo_devolver in sesion["libros_prestados"]:
                        sesion["libros_prestados"].remove(titulo_devolver)
                        for libro in datos_libros:
                            if libro["titulo"] == titulo_devolver:
                                libro["disponibilidad"] = True
                                break
                        adm_libros.write_json(datos_libros)
                        adm_users.write_json(datos_usuarios)
                        print("Libro devuelto con éxito.")
                    else:
                        print("No tienes ese libro, deja de mentir xd")

                elif opcion == "3":
                    print("\n LISTA DE LIBROS ")
                    for libro in datos_libros:
                        print(f"Título: {libro['titulo']} | Autor: {libro['autor']} | Estado: {'disponibilidad'}")

                elif opcion == "4":
                    print("Saliendo...")
                    break
                else:
                  print("Cédula no registrada.")
     
    while True:
        print(" SERVICIO NACIONAL DE BIBLIOTECA COMUNITARIA DE UNEFA:")
        print()
        print("ACTUALIZACIÓN 2026, FELICIDADES, ESPERO NO SIGAS SUBIENDO MÁS :D")
        print()
        print("Cargando opciones...")
        time.sleep(5) # no le pongo más por risa

        option = input("Primera vez? (S/N): ").lower()
        
        if option == "s":
            print("Registrese...")
            nombre_registro = input("pon tu nombre: ")
            cedula_registro = input("y su CI?: ")
            edad = int(input("Coloque su edad: "))
            telefono = input("su numero de telefono: ")
            gmail = input("Y su correo electronico: ")
            
            tipo = input("¿Eres Estudiante o Profesor? (E/P): ")
            tipx = "Profesor" if tipo == "P" else "Estudiante"

            user = {
                "nombre": nombre_registro, 
                "cedula": cedula_registro,
                "edad": edad, 
                "telefono": telefono,
                "gmail": gmail,
                "tipo": tipx,
                "libros_prestados": []
            }

            datos_usuarios.append(user)
            adm_users.write_json(datos_usuarios)
            print(f"Bienvenido, {user['nombre']}. Disfrute del SNBC")
            print()
            menu()

        else:
            cedula_login = input("Jaja, te toca ingresar tu cedula papu :v : ")
            sesion = None

            for nose in datos_usuarios:
                if nose["cedula"] == cedula_login:
                    sesion = nose
                    break

               