class Pet:

    def __init__(self, pet_name, pet_colour):
        # this full list of attributes can be applied to subclasses
        # by including super().__init__(parameters) in the def __init__ for that class
        self._name = pet_name
        self._colour = pet_colour

    # this method doesn't need to be re-defined in the subclasses
    def make_sound(self):
        return "sound"
