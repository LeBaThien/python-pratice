from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class AnimalFactory(ABC):
    @abstractmethod
    def create_dog(self):
        pass

    @abstractmethod
    def create_cat(self):
        pass


class ConcreteAnimalFactory(AnimalFactory):
    def create_dog(self):
        return Dog()

    def create_cat(self):
        return Cat()


if __name__ == '__main__':
    factory = ConcreteAnimalFactory()
    dog = factory.create_dog()
    cat = factory.create_cat()