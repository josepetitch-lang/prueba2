import json

def agregar_tarea():
  tareas = obtener_tareas()
  nombre = input("Ingrese Nombre: ")
  categoria = input("Ingrese Categoria: ")
  identificador = int(input("Ingresa el identificador: "))
  completado = input("Esta completada?(Si/No): ")
  
  if completado.lower() == "si":
    completado = True
  else:
    completado = False 
  
  tareas.append({"id": identificador, "nombre": nombre, "categoria": categoria, "completado": completado})
  
  guardar_tareas(tareas)

def listar_tareas():
  tareas = obtener_tareas()
  for tarea in tareas:
    print(f"{tarea['id']} - {tarea['nombre']} - {tarea['categoria']} - {convertidor_estatus(tarea['completado'])}")

def marcar_completada(id_tarea):
  tareas = obtener_tareas()
  indice_encontrado = buscar_indice_tarea(tareas, id_tarea)
  
  if indice_encontrado == None:  
  # if not indice_encontrado:
    print("Tarea no encontrada")
    return
  else:
    tareas[indice_encontrado]["completado"] = True
  
  guardar_tareas(tareas)
  
  print("Tarea actualizada! \n")
      
def obtener_tareas():
  try:
    with open("tareas.json", "r") as archivo:
      tareas = json.load(archivo)
      return tareas
  except (FileNotFoundError, json.JSONDecodeError):
    return []
    
def convertidor_estatus(estatus):
  if estatus == True:
    return "Completada"
  else:
    return "Pendiente"
  
def buscar_indice_tarea(tareas, id_tarea):
  for tarea in tareas:
    if int(tarea["id"]) == int(id_tarea):
      return tareas.index(tarea)
  
  return None

def guardar_tareas(tareas):
   with open("tareas.json", "w") as archivo:
      json.dump(tareas,archivo)
    
def eliminar_tarea(id_a_eliminar):
    tareas = obtener_tareas()
    Indice = buscar_indice_tarea(tareas, id_a_eliminar)
    if Indice != None:
       tareas.pop(Indice)
       guardar_tareas(tareas)
       print("Tarea eliminada")
    else:
        print("Tarea no existente")


def filtrar_por_categoría(categoria_buscar):
    tareas = obtener_tareas()
    resultadinhos = []

    for tarea in tareas:
        if tarea["categoria"].lower() == categoria_buscar.lower():
            resultadinhos.append(tarea["nombre"])
            
    if resultadinhos:
        for nombre in resultadinhos:
            print(f"- {nombre}")
    else:
        print("NO ENCONTRADAS TAREAS EN ESTA CATEGORÍA")

def resumen_tareas():
    lista_de_tareas = obtener_tareas()
    total = len(lista_de_tareas)
    contador = 0 

    for tarea in lista_de_tareas:
      if tarea['completado'] == True:
          contador = contador + 1
    
    pendientes = total - contador

    print(f"Total de tareas: {total}")
    print(f"Total completado: {contador}")
    print(f"Pendiente: {pendientes}")

    if pendientes == 0:
        print("no hay tareas pendientes... nose si eres un tramposo o un genio, pero feliz día :)")

def new_list(tareas, id_a_eliminar):
   tareas = obtener_tareas()
   box = []

   for tarea in tareas:
      if tarea["id"] != id_a_eliminar:
         box.append(tarea)

   return box 

