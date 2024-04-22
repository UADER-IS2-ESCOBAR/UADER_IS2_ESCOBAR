class IteradorCadena:
    def __init__(self, cadena):
        self.cadena = cadena
        self.posicion = 0
        self.direccion_reversa = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.direccion_reversa:
            if self.posicion <= 0:
                raise StopIteration
            self.posicion -= 1
            return self.cadena[self.posicion]
        else:
            if self.posicion >= len(self.cadena):
                raise StopIteration
            self.posicion += 1
            return self.cadena[self.posicion - 1]

    def reversa(self):
        self.direccion_reversa = True
        self.posicion = len(self.cadena)

    def directa(self):
        self.direccion_reversa = False
        self.posicion = 0


if __name__ == "__main__":
    cadena = "Hola Mundo"
    iterador = IteradorCadena(cadena)

    print("Recorrido en sentido directo:")
    for caracter in iterador:
        print(caracter, end=" ")

    print("\nRecorrido en sentido inverso:")
    iterador.reversa()
    for caracter in iterador:
        print(caracter, end=" ")
