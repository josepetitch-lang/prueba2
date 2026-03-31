def opciones_menu():
    print("1. Agregar tarea")
    print()
    print("2. Lista de tareas")
    print()
    print("3. Marcar tarea como completada")
    print()
    print("4. Salir")
    print()

print("Aplicación de Gestión de Datos")
print()

while True: 
    opciones_menu()

    option = input("Seleccione una opcion:")
    match option:
        case "1":
            print("Agregar tarea")
        case "2":
            print("Lista de tareas")
        case "3":
            print("Marcar Tarea")
        case "4":
            print("bai bai")
            break
        case _:
            print("Invalid option (si, está en ingles, es que es para que escribas tu opción bien >:)")


