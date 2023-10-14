class CuentaBancaria:
    def __init__(self, tasa_interes=0.01, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def deposito(self, amount):
        self.balance += amount

    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5

    def mostrar_balance(self):
        print(f"Balance: ${self.balance}")

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = {}

    def crear_cuenta(self, nombre_cuenta, tasa_interes=0.01, balance=0):
        self.cuentas[nombre_cuenta] = CuentaBancaria(tasa_interes, balance)

    def hacer_deposito(self, nombre_cuenta, amount):
        if nombre_cuenta in self.cuentas:
            self.cuentas[nombre_cuenta].deposito(amount)
        else:
            print(f"La cuenta '{nombre_cuenta}' no existe para {self.nombre}.")

    def hacer_retiro(self, nombre_cuenta, amount):
        if nombre_cuenta in self.cuentas:
            self.cuentas[nombre_cuenta].retiro(amount)
        else:
            print(f"La cuenta '{nombre_cuenta}' no existe para {self.nombre}.")

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}")
        for nombre_cuenta, cuenta in self.cuentas.items():
            print(f"Cuenta: {nombre_cuenta}, Balance: ${cuenta.balance}")

# Ejemplo de uso
usuario1 = Usuario("Alice")
usuario1.crear_cuenta("Cuenta1", tasa_interes=0.02, balance=1000)
usuario1.crear_cuenta("Cuenta2", tasa_interes=0.01, balance=500)
usuario1.hacer_deposito("Cuenta1", 300)
usuario1.hacer_retiro("Cuenta2", 200)
usuario1.mostrar_balance_usuario()
