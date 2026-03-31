# Abstracción
# Encapsulamiento
# Herencia
# Polimorfismo

# Abstracción :Es quedarnos con lo importante para nuestro sistema y dejar por fuera lo que no aporta al contexto actual
# Encapsulamiento: Agruupar datos y metodos que operan sobre otros datos
# Herencia: Capacidad de una clase para heredar atributos y metodos de otra clase
#

class Car:
    def __init__(self, tarifa_diaria, deposito, marca, modelo, placa, cantidad_de_puestos, disponibilidad, estado_de_alquiler):
        self.tarifa_diaria = tarifa_diaria
        self.deposito = deposito
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.cantidad_de_puestos = cantidad_de_puestos
        self.disponibilidad = disponibilidad
        self.estado_de_alquiler = estado_de_alquiler

    def alquiler(self):
        pass

    def calcular_deposito(self):
        pass

    def recibir_vehiculo(self, car):
        pass
    
    def inspeccion_de_entrega(self, car):
        pass

yaris = Car(90, 500, "Toyota", "Yaris", "AAA123", "5", True, "Disponible")


yaris.marca = "Ford"
print(yaris.marca)
