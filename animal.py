#For the inheretence stuff
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def drink(self):
        print(f"{self.name} is drinking.")


# a_dog = Animal("Mia")
# a_dog.eat()
# a_dog.drink()
