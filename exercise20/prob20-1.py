class Vehicle():

    def fuel_efficiency(self):
        return 10
    

class ElectricCar(Vehicle):

    def fuel_efficiency(self):
        return 'N/A'
    

class Truck(Vehicle):

    def fuel_efficiency(self):
        return 5
    

vehicle = Vehicle()
electric_car = ElectricCar()
truck = Truck()

print(f"Vehicle fuel efficiency: {vehicle.fuel_efficiency()} km/l")
print(f"Electric car fuel efficiency: {electric_car.fuel_efficiency()}")
print(f"Truck fuel efficiency: {truck.fuel_efficiency()} km/l")

