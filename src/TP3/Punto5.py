class Avion:
    def __init__(self):
        self.body = None
        self.turbinas = []
        self.alas = []
        self.tren_aterrizaje = None

    def __str__(self):
        return f"Avion: {self.body}, {self.turbinas}, {self.alas}, {self.tren_aterrizaje}"

class ConstructorAvion:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self, body):
        self.avion.body = body

    def construir_turbina(self, turbina):
        self.avion.turbinas.append(turbina)

    def construir_ala(self, ala):
        self.avion.alas.append(ala)

    def construir_tren_aterrizaje(self, tren):
        self.avion.tren_aterrizaje = tren

# Ejemplo de uso
if __name__ == "__main__":
    constructor = ConstructorAvion()
    constructor.construir_body("Body A")
    constructor.construir_turbina("Turbina 1")
    constructor.construir_turbina("Turbina 2")
    constructor.construir_ala("Ala 1")
    constructor.construir_ala("Ala 2")
    constructor.construir_tren_aterrizaje("Tren de Aterrizaje")

    avion = constructor.avion
    print(avion)
