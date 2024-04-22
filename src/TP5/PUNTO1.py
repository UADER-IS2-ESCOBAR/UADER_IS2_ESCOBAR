class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, number):
        if not self.successor:
            return False  # No handler to process the number
        return self.successor.handle(number)


class PrimeHandler(Handler):
    def handle(self, number):
        if number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)):
            print(f"PrimeHandler consumed: {number}")
            return True
        else:
            return super().handle(number)


class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"EvenHandler consumed: {number}")
            return True
        else:
            return super().handle(number)


class DefaultHandler(Handler):
    def handle(self, number):
        print(f"No handler to consume: {number}")
        return True  # Marking as consumed


class NumberChain:
    def __init__(self):
        self.chain = PrimeHandler(EvenHandler(DefaultHandler()))

    def process_numbers(self):
        for number in range(1, 101):
            self.chain.handle(number)


if __name__ == "__main__":
    chain = NumberChain()
    chain.process_numbers()
