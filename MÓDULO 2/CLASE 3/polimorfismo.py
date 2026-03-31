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

