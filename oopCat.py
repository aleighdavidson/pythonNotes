from oopPet import Pet


class Cat(Pet):
    # __init__is very special, python reserved function
    # the constructor method
    def __init__(self, cat_name, cat_colour):
        # instance variable, aka attribute called _name
        # single underscore before name means it is private for the class
        # self._name = cat_name
        # self._colour = cat_colour
        # inheriting from superclass
        super().__init__(cat_name, cat_colour)

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
