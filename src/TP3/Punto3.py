class ComidaRapida:
    def entregar(self):
        pass

class Hamburguesa(ComidaRapida):
    def entregar(self, metodo):
        print(f"Hamburguesa entregada por {metodo}")

class HamburguesaFactory:
    @staticmethod
    def crear_hamburguesa():
        return Hamburguesa()

# Ejemplo de uso
if __name__ == "__main__":
    hamburguesa = HamburguesaFactory.crear_hamburguesa()
    hamburguesa.entregar("mostrador")
    hamburguesa.entregar("cliente")
    hamburguesa.entregar("delivery")
