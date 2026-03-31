import time

from models.usuario import Estudiante, Profesor
from utils.json_manager import JsonManager


adm_libros = JsonManager("libros")
adm_users = JsonManager("usuarios")


datos_libros = adm_libros.read_json()
datos_usuarios = adm_users.read_json()

if __name__ == "__main__": 
    while True:
        print("\n--- SNBC UNEFA ---")
        print("1. Pedir")
        print("2. Entregar")
        print(" 3. Ver")
        print("4. Salir")
        opcion = input("Seleccione: ")

        if opcion == "1":
            id_u = input("ID Usuario: ")
            cod_l = input("Código Libro: ")

            for u in datos_usuarios:
                if u["identificacion"] == id_u:
                    
                    if u("tipo") == "Profesor":
                        user = Profesor(u["nombre"], u["ci"], u["edad"], u["identificacion"], u["correo"], u["libros_prestados"])
                    else:
                        user= Estudiante(u["nombre"], u["ci"], u["edad"], u["identificacion"], u["correo"], u["libros_prestados"])
                    
                   
                    if user.puede_pedir():
                        for l in datos_libros:
                            if l["codigo"] == cod_l and l["disponibilidad"] == True:
                                
                                
                                l["disponibilidad"] = False
                                u["libros_prestados"].append(cod_l)
                                
                                
                                adm_libros.write_json(datos_libros)
                                adm_users.write_json(datos_usuarios)
                                
                                print(f" Prestado: {l['titulo']}")
                                break
                        else:
                            print(" Libro no disponible o no existe.")
                    else:
                        print(f" Límite de libros alcanzado para {u('tipo', 'Estudiante')}.")
                    break
            else:
                print(" Usuario no encontrado.")

        elif opcion == "2": 
            id_u = input("ID Usuario: ")
            cod_l = input("Código Libro: ")

            for u in datos_usuarios:
                if u["identificacion"] == id_u:
                    if cod_l in u["libros_prestados"]:
                        for l in datos_libros:
                            if l["codigo"] == cod_l:
                                l["disponibilidad"] = True
                                u["libros_prestados"].remove(cod_l)
                                
                                adm_libros.write_json(datos_libros)
                                adm_users.write_json(datos_usuarios)
                                print(" Libro devuelto con éxito.")
                                break
                        break
            else:
                print(" No se encontró el registro del préstamo.")

        elif opcion == "3": 
            print("\n--- LISTA DE LIBROS ---")
            for l in datos_libros:
                estado = "DISPONIBLE" 
                print(f"[{l['codigo']}] {l['titulo']} - {estado}")
            time.sleep(1)

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")