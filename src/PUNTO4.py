from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class Radio:
    """
    Clase que representa una radio capaz de almacenar frecuencias en memorias predefinidas.
    """

    def __init__(self):
        self._frecuencias_am = {"M1": None, "M2": None, "M3": None, "M4": None}
        self._frecuencias_fm = {"M1": None, "M2": None, "M3": None, "M4": None}

    def almacenar_frecuencia_am(self, memoria: str, frecuencia: float) -> None:
        self._frecuencias_am[memoria] = frecuencia

    def almacenar_frecuencia_fm(self, memoria: str, frecuencia: float) -> None:
        self._frecuencias_fm[memoria] = frecuencia

    def obtener_frecuencia_am(self, memoria: str) -> float:
        return self._frecuencias_am[memoria]

    def obtener_frecuencia_fm(self, memoria: str) -> float:
        return self._frecuencias_fm[memoria]


class ProcesadorDeComandos:
    """
    El ProcesadorDeComandos ejecuta comandos en función de las solicitudes recibidas.
    """

    def __init__(self, radio: Radio):
        self._radio = radio

    def ejecutar_comando(self, comando: Command) -> None:
        """
        Ejecuta el comando.
        """
        comando.execute()

    def barrer_frecuencias(self) -> None:
        """
        Realiza un ciclo de barrido de frecuencias, incluyendo las memorias AM y FM.
        """
        print("Barrido de frecuencias:")

        for memoria in ["M1", "M2", "M3", "M4"]:
            frecuencia_am = self._radio.obtener_frecuencia_am(memoria)
            if frecuencia_am is not None:
                print(f"Sintonizando AM - Memoria {memoria}: {frecuencia_am}")

            frecuencia_fm = self._radio.obtener_frecuencia_fm(memoria)
            if frecuencia_fm is not None:
                print(f"Sintonizando FM - Memoria {memoria}: {frecuencia_fm}")


class AlmacenarFrecuenciaAM(Command):
    """
    Comando para almacenar una frecuencia en una memoria AM.
    """

    def __init__(self, radio: Radio, memoria: str, frecuencia: float) -> None:
        self._radio = radio
        self._memoria = memoria
        self._frecuencia = frecuencia

    def execute(self) -> None:
        self._radio.almacenar_frecuencia_am(self._memoria, self._frecuencia)


class AlmacenarFrecuenciaFM(Command):
    """
    Comando para almacenar una frecuencia en una memoria FM.
    """

    def __init__(self, radio: Radio, memoria: str, frecuencia: float) -> None:
        self._radio = radio
        self._memoria = memoria
        self._frecuencia = frecuencia

    def execute(self) -> None:
        self._radio.almacenar_frecuencia_fm(self._memoria, self._frecuencia)


if __name__ == "__main__":
    radio = Radio()
    procesador = ProcesadorDeComandos(radio)

    # Almacenar frecuencias en las memorias
    comando_am1 = AlmacenarFrecuenciaAM(radio, "M1", 1000)
    comando_fm2 = AlmacenarFrecuenciaFM(radio, "M2", 90.5)
    procesador.ejecutar_comando(comando_am1)
    procesador.ejecutar_comando(comando_fm2)

    # Barrer las frecuencias almacenadas
    procesador.barrer_frecuencias()
