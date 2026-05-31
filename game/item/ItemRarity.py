from enum import IntEnum

class Rarity(IntEnum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4

    def getColor(self):
        if self == Rarity.COMMON:
            return "white"
        elif self == Rarity.UNCOMMON:
            return "green"
        elif self == Rarity.RARE:
            return "blue"
        elif self == Rarity.EPIC:
            return "purple"
        elif self == Rarity.LEGENDARY:
            return "orange"
        
    def getdropRate(self):
        if self == Rarity.COMMON:
            return 0.83
        elif self == Rarity.UNCOMMON:
            return 0.12
        elif self == Rarity.RARE:
            return 0.04
        elif self == Rarity.EPIC:
            return 0.0095
        elif self == Rarity.LEGENDARY:
            return 0.0005
        
    def getMultiplier(self):
        if self == Rarity.COMMON:
            return 1.0
        elif self == Rarity.UNCOMMON:
            return 1.5
        elif self == Rarity.RARE:
            return 2.0
        elif self == Rarity.EPIC:
            return 3.0
        elif self == Rarity.LEGENDARY:
            return 5.0
    
    def __str__(self):
        return self.name.capitalize()