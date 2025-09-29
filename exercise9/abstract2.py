"""
prob2.py: This file illustrates the usage of an abstract class and DocStrings
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """Class Animal is an abstract class that has abstract method move"""
    @abstractmethod
    def move(self):
        """Method move is an abstract method of an abstract class Animal"""
        pass


class Human(Animal):
    def move(self):
        print('Human can crawl, walk and run')

class Snake(Animal):
    def move(self):
        print('Snake can crawl')

class Dog(Animal):
    def move(self):
        print('Dog can walk and run')


if __name__ == "__main__":
    print(__doc__)
    print(Animal.__doc__)
    print(Animal.move.__doc__)
    print("=== Below is the output of the code ===")
    human = Human()
    human.move()
    snake = Snake()
    snake.move()
    dog = Dog()
    dog.move()