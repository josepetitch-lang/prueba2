import tasks as mt
def opciones_menu():
    print("1. Agregar tarea")
    print()
    print("2. Lista de tareas")
    print()
    print("3. Marcar tarea como completada")
    print()
    print("4. Salir")
    print()
    print("5. Eliminar tarea")
    print()
    print("6. Filtrar por categoría")
    print()
    print("7. Resumen de tareas")
    print()

def datos_tarea():
    nombre = input("Ingrese una tarea:")
    categoría = int(input("Ingrese una categoría"))

    return (f"nombre: {nombre}, categoría: {categoría}")

def pedir_id():
    try:
        return int(input("Ingrese el ID: "))
    except ValueError:
        print("¡Error! Debe ser un número.")
        return None 

print("Aplicación de Gestión de Datos")
print()

while True: 
    opciones_menu()

    option = input("Seleccione una opcion:")
    match option:
        case "1":
            mt.agregar_tarea()
            datos_tarea()
            print("Tarea Agregada")
        case "2":
            print("Lista de tareas")
            mt.listar_tareas()
        case "3":
            print("Marcar Tarea")
            pedir_id()
            mt.marcar_completada(pedir_id)
        case "4":
            print("bai bai")
            break   
        case "5":
            pedir_id()
            mt.eliminar_tarea(pedir_id)
        case "6":
            categoría = input("Coloque la categoría a filtrar:")
            mt.filtrar_por_categoría(categoría)
        case "7":
            mt.resumen_tareas()
        case _:
            print("Opción invalida")

