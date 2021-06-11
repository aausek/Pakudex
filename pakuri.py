# Developed by Ana Ausek - 06/09/2021
from hashlib import md5
import math

# Class
class Pakuri:
    
    # List of instances
    pkList = []
    
    # Constructor
    def __init__(self, name, species, level=0):
        self.__name = name
        self.__species = species
        self._level = level
        
        # Hashing
        hashedName = md5(name.encode())
        hashedSpecies = md5(species.encode())
        hashedNameInt = int.from_bytes(hashedName.digest(), byteorder='little')
        hashedSpeciesInt = int.from_bytes(hashedSpecies.digest(), byteorder='little')
        
        # Attack, Defense, Stamina
        self.__attack = hashedSpeciesInt % 16 + hashedNameInt % 16
        self.__defense = (hashedSpeciesInt + 5) % 16 + (hashedNameInt+ 5) % 16
        self.__stamina = (hashedSpeciesInt + 11) % 16 + (hashedNameInt + 11) % 16
        
        self.__hp = math.floor(self.__stamina * (level/6))
        self.__cp = math.floor(self.__attack * math.sqrt(self.__defense) * math.sqrt(self.__stamina) * level * 0.08)
    
    # Properties of constructor
    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species
    
    @property
    def hp(self):
        return self.__hp
    
    @property
    def cp(self):
        return self.__cp    

    @property
    def level(self):
        return self._level

    def set_level(self, level):
        self._level = level
        self.__hp = math.floor(self.__stamina * (level / 6))
        self.__cp = math.floor(self.__attack * math.sqrt(self.__defense) * math.sqrt(self.__stamina) * level * 0.08)
