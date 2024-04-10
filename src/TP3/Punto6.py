import time
import copy

class Prototipo:
    def __init__(self):
        self.atributo = "Prototipo"

    def clone(self):
        return copy.deepcopy(self)

# Crear instancia prototipo
prototipo = Prototipo()

# Crear 20 anidamientos
for i in range(20):
    print(f"Anidamiento {i + 1} - Creación del objeto...")
    
    # Simular carga de procesamiento de 2 segundos
    time.sleep(2)
    
    # Clonar prototipo
    nuevo_objeto = prototipo.clone()

    print(f"Anidamiento {i + 1} - Objeto creado: {nuevo_objeto}")

print("Creación de objetos finalizada.")
