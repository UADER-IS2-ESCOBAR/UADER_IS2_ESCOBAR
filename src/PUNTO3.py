class Observer:
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, emitted_id):
        if emitted_id == self.observer_id:
            print(f"¡El ID emitido ({emitted_id}) coincide con el ID del observador ({self.observer_id})!")


class ObservadorA(Observer):
    def __init__(self):
        super().__init__("ABCD")

class ObservadorB(Observer):
    def __init__(self):
        super().__init__("EFGH")

class ObservadorC(Observer):
    def __init__(self):
        super().__init__("IJKL")

class ObservadorD(Observer):
    def __init__(self):
        super().__init__("MNOP")


class SujetoObservable:
    def __init__(self):
        self.observers = []

    def agregar_observador(self, observer):
        self.observers.append(observer)

    def eliminar_observador(self, observer):
        self.observers.remove(observer)

    def notificar_observadores(self, emitted_id):
        for observer in self.observers:
            observer.update(emitted_id)


if __name__ == "__main__":
    sujeto = SujetoObservable()

    observador_a = ObservadorA()
    observador_b = ObservadorB()
    observador_c = ObservadorC()
    observador_d = ObservadorD()

    sujeto.agregar_observador(observador_a)
    sujeto.agregar_observador(observador_b)
    sujeto.agregar_observador(observador_c)
    sujeto.agregar_observador(observador_d)

    
    emitted_ids = ["ABCD", "WXYZ", "EFGH", "1234", "IJKL", "5678", "MNOP", "9012"]

    for emitted_id in emitted_ids:
        sujeto.notificar_observadores(emitted_id)
