class Numero:
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        print(f"Valor actual: {self.valor}")
        return self


class OperacionDecorator(Numero):
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        return self.numero.imprimir()


class SumarDos(OperacionDecorator):
    def imprimir(self):
        self.numero.valor += 2
        return super().imprimir()


class MultiplicarPorDos(OperacionDecorator):
    def imprimir(self):
        self.numero.valor *= 2
        return super().imprimir()


class DividirPorTres(OperacionDecorator):
    def imprimir(self):
        self.numero.valor /= 3
        return super().imprimir()


# Ejemplo de uso
if __name__ == "__main__":
    numero = Numero(10)

    print("Operaciones sin decoradores:")
    numero.imprimir()
    print()

    print("Operaciones con decoradores:")
    operacion = SumarDos(MultiplicarPorDos(DividirPorTres(numero)))
    operacion.imprimir()
