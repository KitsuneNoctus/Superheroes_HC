#dog.py
import random
class Dog:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    # Methods are defined as their own named functions inside the class
    def bark(self):
        print("Woof!")

    # def sit(self, name):
    #     print("{} sits".format(name))
    #
    # def roll_over(self, name):
    #     print("{} rolls over".format(name))

# my_dog = Dog("Rex", "Superdog")
# my_dog.bark()
# #print(my_dog)
# #print(my_dog.name)
# print(my_dog.breed)
