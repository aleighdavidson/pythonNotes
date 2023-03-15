class Pet:

    def __init__(self, pet_name, pet_colour):  # constructor
        # this full list of attributes can be applied to subclasses
        # by including super().__init__(parameters) in the def __init__ for that class
        # can pass complex values (lists, dictionaries, other objects) not just primitive
        self._name = pet_name
        self._colour = pet_colour
        # best practice to declare all attributes in the constructor, even if you don't have the value initially

    # this method doesn't need to be re-defined in the subclasses
    def make_sound(self):
        return "sound"
