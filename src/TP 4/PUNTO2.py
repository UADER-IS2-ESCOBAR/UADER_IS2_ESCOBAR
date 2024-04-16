class LaminaAcero:
    def __init__(self, espesor, ancho):
        self.espesor = espesor
        self.ancho = ancho

    def producir(self):
        pass

class TrenLaminador:
    def __init__(self, longitud):
        self.longitud = longitud

    def producir(self):
        pass

class PuenteProduccionLaminaAcero:
    def __init__(self, lamina_acero, tren_laminador):
        self.lamina_acero = lamina_acero
        self.tren_laminador = tren_laminador

    def producir_lamina(self):
        self.tren_laminador.producir()

# Subclases concretas para LaminaAcero
class LaminaAcero05Pulgadas(LaminaAcero):
    def __init__(self, ancho):
        super().__init__(espesor=0.5, ancho=ancho)

class LaminaAcero15MetrosAncho(LaminaAcero):
    def __init__(self, espesor):
        super().__init__(espesor=espesor, ancho=1.5)

# Subclases concretas para TrenLaminador
class TrenLaminador5Metros(TrenLaminador):
    def __init__(self):
        super().__init__(longitud=5)

    def producir(self):
        print(f"Produciendo lámina de acero con una longitud de {self.longitud} metros")

class TrenLaminador10Metros(TrenLaminador):
    def __init__(self):
        super().__init__(longitud=10)

    def producir(self):
        print(f"Produciendo lámina de acero con una longitud de {self.longitud} metros")

# Ejemplo de uso
if __name__ == "__main__":
    lamina05pulgadas = LaminaAcero05Pulgadas(ancho=1.5)
    tren5m = TrenLaminador5Metros()

    puente1 = PuenteProduccionLaminaAcero(lamina05pulgadas, tren5m)
    puente1.producir_lamina()  # Produciendo lámina de acero con una longitud de 5 metros

    lamina15m = LaminaAcero15MetrosAncho(espesor=0.5)
    tren10m = TrenLaminador10Metros()

    puente2 = PuenteProduccionLaminaAcero(lamina15m, tren10m)
    puente2.producir_lamina()  # Produciendo lámina de acero con una longitud de 10 metros
