class Vehiculo:
  def __init__(self, modelo, anio, color, marca):
    self.modelo = modelo
    self.anio = anio
    self.color = color
    self.marca = marca

  def enciende(self):
    print("El Vehiculo esta encendiendo")

  def recarga_gasolina(self, cantidad_de_litros):
    print(f"El vehiculo esta recargando {cantidad_de_litros} litros")

class Carro(Vehiculo):
  def __init__(self, modelo, anio, color, marca, cantidad_de_puertas, tiene_maletera = True):
    super().__init__(modelo, anio, color, marca)
    self.cantidad_de_puertas = cantidad_de_puertas
    self.tiene_maletera = tiene_maletera


class Moto(Vehiculo):
  def __init__(self, modelo, anio, color, marca, activa_delivery):
    super().__init__(modelo, anio, color, marca)
    self.activa_delivery = activa_delivery

camaro = Carro("Camaro", "2020", "Amarillo", "Chevrolet", 2)
bera = Moto("SBR", "2025", "Rojo", "Bera", True)

print(camaro.modelo)
print(camaro.color)
print(camaro.cantidad_de_puertas)
camaro.enciende()
camaro.recarga_gasolina(80)
print()
print(bera.modelo)
print(bera.marca)
bera.recarga_gasolina(15)


# Ejemplo 

print("Ejemplo animales")
print()

class Animal():
  def hacer_sonido(self):
    print("Sonido generico")

class Perro(Animal):
  def hacer_sonido(self):
    print("Wauu")

class Gato(Animal):
  def hacer_sonido(self):
    print("Miauu")

class Vaca(Animal):
  def hacer_sonido(self):
    print("Muuuu")

perro = Perro()
gato = Gato()
# perro.hacer_sonido()
# gato.hacer_sonido()

animales = [Perro(), Gato(), Vaca(), Perro(), Vaca(), Gato()]

for animal in animales:
  animal.hacer_sonido()