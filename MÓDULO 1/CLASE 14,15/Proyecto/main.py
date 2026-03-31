import tecnica as tc

def pomodoro():
    print("Selecciona una de las siguientes opciones")
    print()
    print("1. Colocar actividad")
    print()
    print("2. Establecer temporizador")
    print()
    print("3. Lista de actividades")
    print()
    print("4. Historial")
    print()
    print("5. Salir")
    print()

def datos():
    nombre = input("¿Indique su nombre")
    tarea = input("¿Que tarea en especifico deseas realizar?")
    objetivo = input("¿Qué deseas conseguir?")

    print(f"perfecto, iniciaremos tu programa, {nombre}")
    print(f"tu tarea es {tarea}")
    print(f"tu objetivo es: {objetivo}, suerte")


while True:
    pomodoro()
    option = input("Elija una opción:")
    match option: 
        case "1":
          tc.tema()
          print("Datos colocados, perfecto")
        case "2":
            datos()
            print("Sesión creada")
            tc.sesiones()
            print("Fin de sesión")
        case "3":
            print("Lista de actividades:")
            tc.listaactividades()
        case "4":
            print("Perfecto, aqui tienes tu historial completo")
            tc.historial()
        case "5":
               fin = input("¡Desea salir? (s/n):")
               if fin == "s":
                  print("Perfecto, tenga buen dia")
                  break
        case _:
            print("ERROR 1: Ponga porfavor una de las opciones asignadas")
            break
