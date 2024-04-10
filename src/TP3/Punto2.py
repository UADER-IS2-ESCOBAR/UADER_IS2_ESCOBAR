class CalculadoraImpuestos:
    def calcular_impuestos(self, importe_base):
        iva = importe_base * 0.21
        iibb = importe_base * 0.05
        contribuciones = importe_base * 0.012
        total_impuestos = iva + iibb + contribuciones
        return total_impuestos

# Ejemplo de uso
if __name__ == "__main__":
    importe_base = 1000
    calculadora = CalculadoraImpuestos()
    total_impuestos = calculadora.calcular_impuestos(importe_base)
    print("Total de impuestos:", total_impuestos)
