class Dog:
    def speak(self):
        return "Wook!"


class Cat:
    def speak(self):
        return "Meow!"


class SimpleAnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == 'Dog':
            return Dog()
        elif animal_type == 'Cat':
            return Cat()
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")


if __name__ == '__main__':
    factory = SimpleAnimalFactory()
    animal1 = factory.create_animal('Dog')
    animal2 = factory.create_animal('Cat')

    print(animal1.speak())
    print(animal2.speak())