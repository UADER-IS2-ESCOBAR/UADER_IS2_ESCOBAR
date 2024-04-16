class ComponenteEnsamblado:
    def mostrar(self, nivel=0):
        pass

class Pieza(ComponenteEnsamblado):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Pieza: {self.nombre}")

class Conjunto(ComponenteEnsamblado):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Conjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)

# Creamos las piezas
piezas = [Pieza(f"Pieza{i}") for i in range(1, 5)]

# Creamos los conjuntos
conjunto1 = Conjunto("Sub-Conjunto 1")
conjunto2 = Conjunto("Sub-Conjunto 2")
conjunto3 = Conjunto("Sub-Conjunto 3")

# Agregamos las piezas a los conjuntos
for i in range(4):
    conjunto1.agregar(piezas[i])
    conjunto2.agregar(piezas[i])
    conjunto3.agregar(piezas[i])

# Creamos el conjunto principal
conjunto_principal = Conjunto("Producto Principal")
conjunto_principal.agregar(conjunto1)
conjunto_principal.agregar(conjunto2)
conjunto_principal.agregar(conjunto3)

# Mostramos la estructura del ensamblado
print("Estructura del ensamblado:")
conjunto_principal.mostrar()
