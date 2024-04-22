import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.states = []

    def write(self, string):
        self.content += string

    def save(self):
        memento = Memento(self.file, self.content)
        self.states.append(memento)
        if len(self.states) > 4:
            del self.states[0]  # Mantener solo los últimos 4 estados

    def undo(self, steps=0):
        if steps == 0:
            if self.states:
                memento = self.states.pop()
                self.file = memento.file
                self.content = memento.content
        else:
            if len(self.states) >= steps:
                memento = self.states[-steps]
                self.file = memento.file
                self.content = memento.content

class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, steps=0):
        writer.undo(steps)

if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para deshacer 1 paso")
    caretaker.undo(writer, 1)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para deshacer 2 pasos")
    caretaker.undo(writer, 2)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para deshacer todos los pasos restantes")
    caretaker.undo(writer)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")
