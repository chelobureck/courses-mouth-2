class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting")

class ElectricCar(Vehicle):
    def electro_start(self):
        if __name__ == "__main__":
            print("Electric car starting")

class Tesla(Car, ElectricCar):
    def start(self):
        super().start()
        print("Tesla ready")

tesla = Tesla()
tesla.start()
