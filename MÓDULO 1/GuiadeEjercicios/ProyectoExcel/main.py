import json
import openpyxl

with open("estudiantes.json", "r") as archivo:
    students = json.load(archivo)

name = input("Hola, usted es el profesor... :")

print(f"Oh, Professor {name}, como olvidarme de usted si fue quien me rayó la mesa el otro día,")

print("Su lista de estudiantes es...")

def students_list():
    for tring in students:
        print(f"Professor: {name}")
        print("Sección: 3° Año [B]")
        print(f"Nombre: {tring['nombre']} {tring['Apellido']} | Edad: {tring['Edad']} | Cedula: {tring['Cedula']}") 
        print(f"repitientes: 1")
students_list()
print("Lista culminada tío")


def agg_excel():
    estudiantes = []
    grupo = ["nombre", "Apellido", "Edad", "Cedula"]

    while True:
        print(f"Bienvenido, {name}")
        nombre = input("Coloque nombre del estudiante")
        apellido = input("Perfecto, sigue el apellido")
        edad = int(input("Coloque la edad"))
        ci = int(input("Y su numero de cedula"))

        estudiantes.append([nombre, apellido, edad, ci])

        proceso = input("¿Desea agregar otro estudiante? (si/no)")
 
        if proceso.lower() == "no":
            print("Perfecto")
            break 

        wb = openpyxl.workbook()
        hoja= wb.active
        hoja.append(grupo)

        for estudiante in estudiantes:
            hoja.append(estudiante)

    wb.save("editable.xlsx")
    print("Archivo editable.xlsx editado y guardado perfectamente :)")
        


