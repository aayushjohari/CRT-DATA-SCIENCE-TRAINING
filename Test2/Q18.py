
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}")


class Car(Vehicle):
    def __init__(self, brand, color, model):
        super().__init__(brand, color) 
        self.model = model

    def show_info(self):
        super().show_info()
        print(f"Model: {self.model}")


my_car = Car("Toyota", "Red", "Corolla")
my_car.show_info()
