from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
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
    human = Human()
    human.move()
    snake = Snake()
    snake.move()
    dog = Dog()
    dog.move()