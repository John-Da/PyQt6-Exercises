class WeatherStation:
    stationCount = 0

    def __init__(self, location, temperature):
        self.__location = location
        self.__temperature = temperature
        WeatherStation.stationCount += 1
        self.__id = WeatherStation.stationCount

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    def get_location(self):
        return self.__location

    def set_location(self, new_location):
        self.__location = new_location

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, new_temperature):
        self.__temperature = new_temperature

    def __str__(self):
        temp_fahrenheit = WeatherStation.celsius_to_fahrenheit(self.__temperature)
        return f"Weather Station WS-{self.__id:03} at {self.__location}:  Temperature: {self.__temperature}°C ({temp_fahrenheit:.1f}°F)"


station1 = WeatherStation("New York", 22.5)
station2 = WeatherStation("Los Angeles", 28.3)

print(station1)
print(station2)

print(f"35°C is {WeatherStation.celsius_to_fahrenheit(35):.1f}°F")
