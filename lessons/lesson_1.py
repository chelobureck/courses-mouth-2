# рок 1. OOП 1: Основы ООП, Создание первых классов, Атрибуты и Методы классов, Принцип ООП - Наследование.

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def drive_to_location(self, location):
        print(f"The car {self.model} is driving to {location}.")

car_honda = Car("honda", "red")

car_subaru = Car("subaru", "blue")

print(car_honda)
print(f"car model: {car_honda.model} car color: {car_honda.color}")
print(car_subaru)
print(f"car model: {car_subaru.model} car color: {car_subaru.color}")

car_honda.drive_to_location("New York")