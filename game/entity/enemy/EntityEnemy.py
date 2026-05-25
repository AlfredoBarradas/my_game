from game.entity.EntityLiving import EntityLiving

class EntityEnemy(EntityLiving):
    def __init__(self, name, life):
        self.name = name
        self.life = life

    pass