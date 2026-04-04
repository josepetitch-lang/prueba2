# Polimorfismo: Significa que diferentes objetos pueden responder al mismo metodo de manera distinta

# Polimorfismo aplicado sin herencia

class PDF:
  def abrir(self):
    print("Abriendo el pdf")

class Xlsx:
  def abrir(self):
    print("Abriendo el excel")

class Docx:
  def abrir(self):
    print("Abriendo el archivo word")

archivos = [PDF(), Xlsx(), Docx()]

for archivo in archivos:
  archivo.abrir()

# Polimorfismo Aplicado en Herencia

class Notificacion:
  def __init__(self, mensaje):
    self.mensaje = mensaje

  def enviar_mensaje(self):
    print(f"Enviando mensaje: {self.mensaje}")

class NotificacionCorreo(Notificacion):
  def __init__(self, mensaje, correo_destinatario):
    super().__init__(mensaje)
    self.correo_destinatario = correo_destinatario

  def enviar_mensaje(self):
    print(f"Enviando mensaje: {self.mensaje} al correo {self.correo_destinatario}")

class NotificacionWhatsapp(Notificacion):
  def __init__(self, mensaje, numero_de_telefono):
    super().__init__(mensaje)
    self.numero_de_telefono = numero_de_telefono

  def enviar_mensaje(self):
    print(f"Enviando mensaje: {self.mensaje} al numero {self.numero_de_telefono}")


mensaje_ws = NotificacionWhatsapp("Hola como estas? Te recordamos ...", "+584123456789")
mensaje_email = NotificacionCorreo("Hola como estas? Esto es un recordatorio ...", "test@prueba.com")

notificaciones = [mensaje_ws, mensaje_email, Notificacion("Esto es una prueba")]

for notificacion in notificaciones:
  notificacion.enviar_mensaje()

class Ysea_tranquilo:
    def hablar(self):
        print("Hola alumnos")

class Ysea_arrecho(Ysea_tranquilo):
    def hablar(self):
        print("Te vamos a mandar a la UNEFM si seguis de alzaito")

class Petit(Ysea_tranquilo):
    def hablar(self):
        print("triquitracatelas")

def volao(profe):
    profe.hablar()

volao(Ysea_arrecho())
volao(Petit())

