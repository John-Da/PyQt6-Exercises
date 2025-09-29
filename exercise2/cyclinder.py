import math


radius = input("Enter radius:")
radius = float(radius)
if radius < 0:
    print("Please enter a positive number for radius")
    exit()


height = input("Enter height:")
height = float(height)
if height < 0:
    print("Please enter a positive number for height")
    exit()

else:
    calculation = 2 * math.pi * radius * (radius + height)
    print(f"The surface area of a cylinder with radius {radius:.2f} and height {height:.2f} is {calculation:.2f}")







