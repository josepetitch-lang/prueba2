estudiantes = []

while True:
  opcion = input("Coloque 1 para ingresar un nuevo estudiante y 2 para salir")
  
  match opcion:
    case "1":
      nombre = input("Indique el nombre del estudiante: ")
      ci = input("Indique la cedula del estudiante: ")
      estudiantes.append({"nombre": nombre, "ci": ci})
    case "2":
      print("Hasta luego")
      break
    case _:
      print("Esta opcion no es valida")

with open("ejercicio_1.txt", "w") as archivo:
  for estudiante in estudiantes:
    archivo.write(f"{estudiante['nombre']}, {estudiante['ci']} \n")