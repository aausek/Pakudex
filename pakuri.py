# Developed by Ana Ausek - 06/09/2021

# Class
class Pakuri:
    # Constructor
    def __init__(self, name, species, level=0):
        self.__name = name
        self.__species = species
        self.level = level

    # Level getter method
    def get_level(self):
        return self.level

    # Level setter method
    def set_temperature(self, level):
        if level < 0:
            raise ValueError('Level cannot be negative.')
        elif level > 500:
            raise ValueError('Maximum level for Pakuri is 50.')
        elif level != int:
            raise ValueError('Invalid level!')
        else:
            self.level = level
