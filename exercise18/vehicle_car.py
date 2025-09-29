# define class Vehicle with brand, model, and year as parameters
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        return f"This vehicle has moved"

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"


# define class Car that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year, doors, fuel):
        super().__init__(brand, model, year)
        self.doors = doors
        self.fuel = fuel

    def move(self):
        return f"This car has been driven"

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}, {self.doors} doors, {self.fuel} fuel"


# Demonstrate the use of inheritance
if __name__ == "__main__":
    # Create a Vehicle instance
    bike = Vehicle("Harley-Davidson", "Street 750", 2022)
    print("Vehicle Information:")
    print(bike.display_info())

    print("\nCar Information:")
    # Create a Car instance
    car = Car("Toyota", "Corolla", 2023, 4, "Gasoline")
    print(car.display_info())

    # Demonstrate inheritance
    print("\nDemonstrating inheritance:")
    print(f"Is car an instance of Vehicle? {isinstance(car, Vehicle)}")
    print(f"Is bike an instance of Car? {isinstance(bike, Car)}")

    # Demostrate overriding methods
    print("\nDemonstrating overriding methods:")
    print(bike.move())
    print(car.move())
