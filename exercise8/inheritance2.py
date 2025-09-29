class Car:

    def __init__(self, make, model, year, mileage=0):
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage

    def drive(self, distance):
        self._mileage = distance

    def __str__(self):
        return f"{self._year} {self._make} {self._model}, Mileage: {self._mileage}"


class RentalCar(Car):
    def __init__(self, make, model, year, dailyrate, mileage=0):
        super().__init__(make, model, year, mileage)
        self._totalCost = 0
        self._is_rented = False
        self._dailyRate = dailyrate

    def rent(self, days):
        self._is_rented = True
        self._totalCost = days * self._dailyRate
        return f"Rented for {days} days. Total cost: ${self._totalCost}"

    def return_car(self, distance_driven):
        self._mileage += distance_driven
        self._is_rented = False
        return f"Car returned."

    def __str__(self):
        if self._is_rented:
            rented = "Rented"
            return (
                f"{super().__str__()}, Daily rate: ${self._dailyRate}, Status: {rented}"
            )

        else:
            avialble = "Available"
            return f"{super().__str__()}, Daily rate: ${self._dailyRate}, Status: {avialble}"


civic = Car("Honday", "Civic", 2021)
civic.drive(1000)
print(civic)
rental_car = RentalCar("Toyota", "Camry", 2022, 50)
print(rental_car)
print(rental_car.rent(3))
print(rental_car)
print(rental_car.return_car(100))
print(rental_car)
