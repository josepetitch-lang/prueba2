
class Usuario:
    def __init__(self, nombre, ci, edad, identificacion, correo):
        self.nombre = nombre
        self.ci = ci
        self.edad = edad
        self.identificacion = identificacion
        self.correo = correo

    def to_dict(self):
     return {
      "nombre": self.nombre,
      "ci": self.ci,
      "edad": self.edad,
      "id:": self.identificacion,
      "correo": self.correo
     }

    def mostrar_informacion(self):
        return f"Usuario: {self.nombre} | ID: {self.identificacion}"

class Estudiante(Usuario):
    def __init__(self, nombre, ci, edad, identificacion, correo, libros_prestados=None):
        super().__init__(nombre, ci, edad, identificacion, correo, libros_prestados)
        self.tipo = "Estudiante"

    def puede_pedir(self):
        return len(self.libros_prestados) < 5

class Profesor(Usuario):
    def __init__(self, nombre, ci, edad, identificacion, correo, libros_prestados=None):
        super().__init__(nombre, ci, edad, identificacion, correo, libros_prestados)
        self.tipo = "Profesor"

    def puede_pedir(self):
        return True