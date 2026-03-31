import json

def tema(): 
    programa = []
    while True:
      asignatura = input("¿Que asignatura es?:")
      contenido = input("¿Que contenido en especifico es:")
      nueva_idea = {"asignatura": asignatura, "contenido": contenido, "status": "pendiente"}
      programa.append(nueva_idea)

      print(f"asignatura: {asignatura}, contenido; {contenido}")
      continuar = input("¿Desea agregar otra idea?")
      if continuar.lower() == "no":
        with open("datos.json", "w") as archivo:
                json.dump(programa, archivo)
        print("Perfecto, tenga un lindo dia")
        break 

def sesiones():

    number = int(input("De que tantos minutos desea establecer su sesión?:"))
    import time
    for i in range(number,0,-1):
        print(f"Quedan: {i} minutos")
        time.sleep(60)
      
    fin_sesion = [{"number": number, "status": "completado"}]

    with open("datos.json", "w") as archivo:
       json.dump(fin_sesion, archivo)
    for i in fin_sesion:
       print(f"tiempo; {i['number']}, status {i['status']}")

def listaactividades():
    
    with open("datos.json", "r") as archivo:
       datos = json.load(archivo)
   
    for actividades in datos:
       print(f"tema {actividades['asignatura']} contenido:{actividades['contenido']}, status: {actividades['status']}")
       return datos

def historial():
     historial = []
     print("Historial de tu mierda: ")
     tareas = listaactividades ()
     for i in tareas:
        if i["status"] == "completado":
           historial.append(f"tema {i['asignatura']}, contenido: {i['contenido']}, status: {i['status']}")
