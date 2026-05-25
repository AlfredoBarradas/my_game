from game.Inventory import Inventory

class InventoryLarge(Inventory):
    def __init__(self, name, lowerSide, upperSide): 
        self.name = name
        self.lowerSide = lowerSide
        self.upperSide = upperSide

    def getInvName(self):
        return self.name
    
    def getSizeInventory(self):
        return self.lowerSide.getSizeInventory() + self.upperSide.getSizeInventory()
    
    def getStackInSlot(self, slot):
        if slot >= self.upperSide.getSizeInventory():
            return self.lowerSide.getStackInSlot(slot - self.upperSide.getSizeInventory())
        else:
            return self.upperSide.getStackInSlot(slot)
        
    def decrStackSize(self, slot, size):
        if slot >= self.upperSide.getSizeInventory():
            return self.lowerSide.decrStackSize(slot - self.upperSide.getSizeInventory(), size)
        else:
            return self.upperSide.decrStackSize(slot, size)
    
    def setInventorySlotContents(self, slot, stack):
        if slot >= self.upperSide.getSizeInventory():
            return self.lowerSide.setInventorySlotContents(slot - self.upperSide.getSizeInventory(), stack)
        else:
            return self.upperSide.setInventorySlotContents(slot, stack)

    def getInventoryStackLimit(self):
        return self.upperSide.getInventoryStackLimit()