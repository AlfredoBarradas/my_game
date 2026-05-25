from game.item.ItemRarity import Rarity

class Item:
    TOTAL_STACK_SIZE = 20

    def __init__(self, items, itemId, rarity=Rarity.COMMON):
        self.items = items
        self.itemId = itemId
        self.maxStackSize = self.TOTAL_STACK_SIZE
        self.rarity = rarity

    def getRarity(self):
        return self.rarity
    
    def getItemId(self):
        return self.itemId