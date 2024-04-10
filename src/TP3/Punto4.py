from abc import ABC, abstractmethod

class Factura(ABC):
    @abstractmethod
    def generar_factura(self, importe):
        pass

class FacturaIVAResponsable(Factura):
    def generar_factura(self, importe):
        total = importe * 1.21  # IVA del 21%
        print(f"Factura para IVA Responsable - Importe: {total}")

class FacturaIVANoInscripto(Factura):
    def generar_factura(self, importe):
        total = importe  # No se aplica IVA
        print(f"Factura para IVA No Inscripto - Importe: {total}")

class FacturaIVAExento(Factura):
    def generar_factura(self, importe):
        print(f"Factura para IVA Exento - Importe: {importe}")

# Ejemplo de uso
if __name__ == "__main__":
    importe = 1000
    
    factura_responsable = FacturaIVAResponsable()
    factura_responsable.generar_factura(importe)
    
    factura_no_inscripto = FacturaIVANoInscripto()
    factura_no_inscripto.generar_factura(importe)
    
    factura_exento = FacturaIVAExento()
    factura_exento.generar_factura(importe)
