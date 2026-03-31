# Programación Orientada a Objetos (POO)

# Componentes principales de la POO:

# Clase -> Plantilla o molde para crear objetos
# Objeto -> Instancia de una clase(Entidad)
# Atributos -> Características o propiedades de una clase u objeto
# Métodos -> Funciones definidas dentro de una clase que describen el comportamiento de un objeto
# Constructor -> Método especial que se llama al crear un objeto y se utiliza para inicializar atributos

# Puntos a tener en cuenta:

# Instancia
# Clase vs objeto
# self dentro de una clase


# PascalCase -> Se utiliza para nombrar clases
# camelCase
# snake_case -> Esta la utilizamos en python para nombre funciones, archivos y variables
# kavac-case

# Ejemplo: 

class Empresa: #"Empresa" (se lo pongo así por gusto, no me mates :( jaja)
    def __init__(self, nombre, especialidad, ubicacion, jefe):
        self.nombre = nombre
        self.especialidad = especialidad
        self.ubicación = ubicacion
        self.jefe = jefe

    def presentación(self):
        return f"Bienvenido, nosotros somos {self.nombre}, nuestra especialidad es {self.especialidad}"
    
    def comunicación(self):
        print(f"Si quiere comunicarse con {self.nombre}, dirijase a {self.jefe}")

empresa1 = Empresa("Nintendo", "Videojuegos", "Japón", "S.Furukawa")
empresa2= Empresa("Coderhub", "Programación", "Venezuela", "D. Marin") #XDDDDDDDD
print(empresa1.jefe)
print(f" Bienvenido a {empresa2.nombre}")

