class Factorial:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def calcular_factorial(self, n):
        if n < 0:
            raise ValueError("El número debe ser no negativo")
        if n == 0 or n == 1:
            return 1
        return n * self.calcular_factorial(n - 1)

# Ejemplo de uso
if __name__ == "__main__":
    factorial = Factorial()
    resultado = factorial.calcular_factorial(5)
    print("El factorial de 5 es:", resultado)
