
class Usuario:
    def __init__(self, nombre, ci, edad, telefono, correo):
        self.nombre = nombre
        self.ci = ci
        self.edad = edad
        self.telefono = telefono
        self.correo = correo

    def to_dict(self):
     return {
      "nombre": self.nombre,
      "ci": self.ci,
      "edad": self.edad,
      "telefono:": self.telefono,
      "correo": self.correo
     }

    def mostrar_informacion(self):
        return f"Usuario: {self.nombre} | CI: {self.ci}"

class Estudiante(Usuario):
    def __init__(self, nombre, ci, edad, telefono, correo, libros_prestados=None):
        super().__init__(nombre, ci, edad, telefono , correo, libros_prestados)
        self.tipo = "Estudiante"

    def puede_pedir(self):
        return len(self.libros_prestados) < 5

class Profesor(Usuario):
    def __init__(self, nombre, ci, edad, telefono , correo, libros_prestados=None):
        super().__init__(nombre, ci, edad, telefono, correo, libros_prestados)
        self.tipo = "Profesor"

    def puede_pedir(self):
        return True