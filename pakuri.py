# Developed by Ana Ausek - 06/09/2021

# Class
class Pakuri:
    instances = set()
    pkCount = 0

    # Constructor
    def __init__(self, name, species, level=0):
        self.__name = name
        self.__species = species
        # self.__hp = hp
        # self.__cp = cp
        self.level = level
        Pakuri.pkCount += 1
        Pakuri.instances.add(self)

    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

    # @property
    # def hp(self):
    #     return self.__hp
    
    # @property
    # def cp(self):
    #     return self.__cp    

    @property
    def level(self):
        return self.level

    @level.setter
    def level(self, level):
        self.level = level

    # # Level setter method
    # def set_level(self, level):
    #     if level < 0:
    #         raise ValueError('Level cannot be negative.')
    #     elif level > 500:
    #         raise ValueError('Maximum level for Pakuri is 50.')
    #     elif level != int:
    #         raise ValueError('Invalid level!')
    #     else:
    #         self.level = level

    def add(self, name, species, hp, cp, level=0):
        obj = Pakuri(name, species, hp, cp)
        instances.add(obj)
