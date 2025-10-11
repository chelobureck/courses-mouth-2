class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting")

class ElectricCar(Vehicle):
    def electro_start(self):   # переименовал метод, чтобы вызов super().start() проходил мимо ElectricCar и шел к Vehicle
        print("Electric car starting")

class Tesla(Car, ElectricCar):
    def start(self):
        super().start()
        print("Tesla ready")

tesla = Tesla()
tesla.start()