class PlayerInventory:
    def __init__(self, player):
        self.player = player
        self.currentItem = 0
        self.mainInventory = [None] * 4
        self.armorInventory = [None] * 4
        ## self.neckInventory = [None] * 2

    pass