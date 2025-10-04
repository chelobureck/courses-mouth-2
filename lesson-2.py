# Урок 2. OOП 2: Другие принципы ООП - Инкапсуляция, Полиморфизм

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def drive_to_location(self, location):
        print(f"The car {self.model} is driving to {location}.")

class Bus(Car):
    def __init__(self, model, color, capacity):
        super().__init__(model, color)
        self.capacity = capacity
    
    def drive_to_location(self, location):
        print(f"The bus {self.model} with capacity {self.capacity} is driving to {location}.")