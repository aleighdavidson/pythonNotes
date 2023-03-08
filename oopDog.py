from oopPet import Pet


class Dog(Pet):

    def __init__(self, dog_name, dog_colour):
        # self._name = dog_name
        # inherit from superclass
        super().__init__(dog_name, dog_colour)

    def bark(self):
        print("Woof woof")

# there are some special methods for doing things with objects
# e.g. you can't directly print an object, it will say the type (object) and it's location in the memory
# if you make a def __str__ method in the class, THAT string will be returned instead
# you can re-define equals (i.e. what does it mean for two objects to be the same
