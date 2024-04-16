import os

class Ping:
    def execute(self, ip_address):
        if ip_address.startswith("192."):
            for _ in range(10):
                response = os.system(f"ping -c 1 {ip_address} > /dev/null 2>&1")
                if response == 0:
                    print(f"Ping to {ip_address} successful!")
                else:
                    print(f"Ping to {ip_address} failed.")
        else:
            print("Invalid IP address. Must start with '192.'")

    def executefree(self, ip_address):
        for _ in range(10):
            response = os.system(f"ping -c 1 {ip_address} > /dev/null 2>&1")
            if response == 0:
                print(f"Ping to {ip_address} successful!")
            else:
                print(f"Ping to {ip_address} failed.")

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)

# Ejemplo de uso:
ping_proxy = PingProxy()
ping_proxy.execute("192.168.0.1")  # Realiza pings a la dirección IP
ping_proxy.execute("8.8.8.8")       # Mensaje de dirección IP inválida
ping_proxy.execute("192.168.0.254") # Realiza ping a www.google.com a través de Ping.executefree
