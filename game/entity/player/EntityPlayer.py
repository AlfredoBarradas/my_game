from game.entity.EntityLiving import EntityLiving

class EntityPlayer(EntityLiving):
    MAX_HEALTH = 100
    RESISTANCE = 10

    def __init__(self, name):
        self.name = name
        self.life = EntityPlayer.MAX_HEALTH

    def getLife(self):
        return self.life

    def getMaxLife(self):
        return EntityPlayer.MAX_HEALTH

    def atributes(self):
        print(f"Player: {self.name}")
        print(f"Health: {self.life}/{EntityPlayer.MAX_HEALTH}")
        print(f"Resistance: {EntityPlayer.RESISTANCE}")

    pass