# diccionario:

investigación = {
          "Criminal 1": {
              "nombre": "Antony",
               "apellido": "Da Souza",
               "edad": "25", 
               "telefono": "0424-560-3939"
           },
           "Victima 1": {
               "Nombre": "Carlos",
                "Apellido": "Noguera",
                "Edad": "30",
                 "Telefono": "0424-330-2220"
            }
}

nuevoestudiante = {
    "Ingreso": {
        "Nombre y Apellido": "Luis Milla",
        "Edad": "18",
        "Carrera": "Ing. de Sistemas",
        "Fecha de Nacimiento": "07/11/2007",
        "Cédula": "V32265890",
        "notas": [5, 2, 30, 12],
        "Dirección": {"Sector": "Puerta Maraven", "Calle": "El Señorial", "Casa": "04"}
    }
}

# CRUD

#READ & UPDATE

nuevoestudiante["Ingreso"]["notas"][0] = 4

nuevoestudiante["Ingreso"]["Sexo"] = "M"

print("Claves:", nuevoestudiante.keys())
print("Valores", nuevoestudiante.values())

NotasEstudianteCurso = "09"  #XDDDDDD

for clave in nuevoestudiante.keys():
    print(clave)

if clave == "Carrera":
    print(f"estoy en {nuevoestudiante[clave]} ")
#DELETE

# del

#PascalCase : Nota Estudiante
#camelCase : parseFloat
#snake_case : notas_estudiante
#kavac-case : notas-estudiante


