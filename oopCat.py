from oopPet import Pet


class Cat(Pet):
    # class variable
    # accessible directly through the class name
    number_of_cats = 0

    # __init__is very special, python reserved function
    # the constructor method
    def __init__(self, cat_name: str, cat_colour: str):  # type hinting
        # instance variable, aka attribute called _name
        # single underscore before name means it is private for the class
        # self._name = cat_name
        # self._colour = cat_colour
        # inheriting from superclass
        super().__init__(cat_name, cat_colour)
        # using the class variable
        Cat.number_of_cats += 1

# type hinting is not enforced, because pythong is interpreted, not compiled language
# in other languages which are compiled, it checks whether the variable types match what has been asked for
    # and will not even run the code

    # method
    def purr(self):
        print("Purr purr")

    def hunt(self, thing):
        print(f"Yum yum, I'm hunting a {thing}.")

    # getter method (returns attributes)
    def get_name(self):
        return self._name + " is " + self._colour

    # setter method
    def set_height(self, cat_height):
        self._height = cat_height

# the methods within the Class can contain anything that we have done previously
# ifs, loops, inputs, returns, etc