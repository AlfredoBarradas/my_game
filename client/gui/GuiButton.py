from client.gui.Gui import Gui
from pyglet import shapes

class GuiButton(Gui):
    def __init__(self, id, x, y, width, height, string=None, color=(0.0,0.0,0.0)):
        super().__init__(x, y, width, height)
        self.displayString = string
        self.color = color
        self.id = id

    def draw(self):
        if not self.visible:
            return
        button = shapes.Rectangle(self.xPos, self.yPos, self.width, self.height, color=self.color)
        button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        onButton = (self.xPos <= x <= self.xPos + self.width and 
                    self.yPos <= y <= self.yPos + self.height)
        if onButton:
            return
    