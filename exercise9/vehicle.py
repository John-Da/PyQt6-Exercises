from abc import ABC, abstractmethod
from datetime import datetime

class Vehicle(ABC):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.curYear = self.diff_year(year)

    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def start_engine(self):
        return f"The {self.make} {self.model}'s engine starts."
    
    @abstractmethod
    def fuel_efficiency(self):
        pass

    @staticmethod
    def diff_year(year):
        curYear = datetime.now()
        years = int(curYear.year) - year
        return years
        


class Car(Vehicle):
    def __init__(self, make, model, year, door):
        super().__init__(make, model, year)
        self.door = door

    def num_doors(self):
        pass

    def fuel_efficiency(self):
        return 30.0 - self.curYear * 0.1


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, sidecar):
        super().__init__(make, model, year)
        self.sidecar = sidecar

    def has_sidecar(self):
        if self.sidecar:
            return True
        else:
            return False

    def fuel_efficiency(self):
        based_efficiency = 50.0
        if self.sidecar:
            based_efficiency -= 5.0
            return based_efficiency - self.curYear * 0.2
        else:
            return based_efficiency - self.curYear * 0.2
        



if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2020, 4)
    motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, False)

    vehicles = [car, motorcycle]
    for vehicle in vehicles:
        print(str(vehicle))
        print(vehicle.start_engine())
        print(f"Fuel Efficiency: {vehicle.fuel_efficiency():.2f} mpg")
        print()