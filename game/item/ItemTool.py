from game.item.Item import Item

class ItemWeapon(Item):
    def __init__(self, items, itemId, strength,):
        super().__init__(items, itemId)
        self.maxDamage = 1 + (strength * 1)

    
