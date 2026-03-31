#Encapsulamiento: Consiste en reunir la información/datos de una clase para definir el comportamiento de una clase para definir el comportamiento de los 
# atributos y métodos para controlar como se usan o modifican dentro del sistema

class CuentaBancaria():
    def __init__(self, tipo_de_cuenta, numero_de_cuenta, titular, saldo = 0):
        self.tipo_de_cuenta = tipo_de_cuenta
        self.numero_de_cuenta = numero_de_cuenta
        self.titular = titular
        self._saldo = saldo

    def obtener_saldo(self):
        return self._saldo

    def deposito(self, monto):
        if monto > 0:
            self._saldo += monto

        return("Saldo en la cuenta actualizado")

    def retiro(self, monto):
        if self._saldo >= monto:
            self._saldo -= monto
            return(f"Se debitaron {monto} de tu cuenta, tu nuevo saldo es {self._saldo}")
        else:
            return("estás acabado")

cuenta1 = CuentaBancaria("Corriente", "012345678", "José Petit", "50000")
print(cuenta1._saldo)
cuenta1._saldo = 100000
print(cuenta1._saldo)
print(cuenta1.obtener_saldo())

class Car:
    LIMITE_VELOCIDAD = 200

    def __init__(self, marca, modelo, limite_velocidad = 200):
        self.marca = marca
        self.modelo = modelo
        self._velocidad = 0
        self._encendido = False
        self.limite_velocidad = limite_velocidad

    def encender(self):
        self._encendido = True

        print("Se prendió esa vaina papu pro")

    def apagar(self):
        if self._velocidad == 0:
            print("Holi, se apagó :3")
        else:
            print("tu madre, eso sigue prendido, apagalo de una vez ")

    def acelerar(self, incremento):
        pass

