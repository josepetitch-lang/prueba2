class Book:
   def __init__(self,autor, título, categoría, disponibilidad):
      self.autor = autor
      self.titulo = título
      self.categoría = categoría
      self.disponibilidad = disponibilidad

   def to_dict(self):
    return {
      "titulo": self.titulo,
      "autor": self.autor,
      "categoria": self.categoria,
      "codigo": self.codigo,
      "disponibilidad": self.disponibilidad
    }

   def prestar(self):
        if self.disponibilidad:
            self.disponibilidad = False
            return f"Préstamo realizado: {self.titulo}"
        else:
          return f"Error: {self.titulo} no está disponible actualmente."

   def devolver(self):
        self.disponibilidad = True
        return f"Gracias por devolver '{self.titulo}' a la biblioteca."

   def esta_disponible(self):
      return self.disponibilidad

   def mostrar_info(self):
        estado = "Disponible" if self.disponibilidad else "Prestado"
        return f"[{self.codigo}] {self.titulo} - {self.autor} ({estado})"