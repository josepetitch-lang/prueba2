import json

def obtener_tareas():
    try:
        with open("tareas.json", "r") as archivo:
            tareas = json.load(archivo)
        return tareas
    except (FileNotFoundError):
        return []

def agregar_tarea():
    # El código asume que 'nombre' ya viene de un paso previo o input
    nombre = input("Nombre de la tarea: ") 
    categoria = input("Ingrese Categoria: ")
    completado = input("Esta completada?(Si/No): ")

    if completado.lower() == "si":
        completado = True
    else:
        completado = False

    tareas = obtener_tareas()
    tareas.append({"nombre": nombre, "categoria": categoria, "completado": completado})

    with open("tareas.json", "w") as lista_tareas:
        json.dump(tareas, lista_tareas)

def listar_tareas():
    tareas = obtener_tareas()
    for tarea in tareas:
        # Se usa la función convertidor_estatus para mostrar un texto amigable
        print(f"{tarea['nombre']} - {tarea['categoria']} - {convertidor_estatus(tarea['completado'])}")



def convertidor_estatus(estatus):
    if estatus == True:
        return ("Completada")
    else:
        return ("Pendiente")

