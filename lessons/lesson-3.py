# Урок 3. Магические, статичные, классовые методы в классах, множественное наследование.

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.__fined = False  # Protected attribute
    
    def drive_to_location(self, location):
        print(f"The car {self.model} is driving to {location}.")
    
    def __test_car(self):  # Protected method
        print(self.model, self.__fined)

    # геттер и сеттер
    def get_fined(self):
        return self.__fined
    
    def set_fined(self, fined_status):
        self.__fined = fined_status

class Bus(Car):
    def __init__(self, model, color, capacity):
        super().__init__(model, color)
        self.capacity = capacity
    
    def drive_to_location(self, location):
        print(f"The bus {self.model} with capacity {self.capacity} is driving to {location}.")

car1 = Car("Toyota", "Red")
bus1 = Bus("Mercedes", "Blue", 50)
# Полиморфизм
car1.drive_to_location(location="Downtown")
bus1.drive_to_location(location="Airport")

vehicles = [car1, bus1]
for v in vehicles:
    v.drive_to_location(location="City Center")


# инкапсуляция
# car1.__fined = True  # Accessing protected attribute (not recommended)
# print(car1.__fined)
# car1.__test_car()  # Accessing protected method (not recommended)

