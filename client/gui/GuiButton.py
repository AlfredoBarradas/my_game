from pyglet import shapes
from pyglet import text

from client.gui.Gui import Gui

class GuiButton(Gui):
    def __init__(self, id, x, y, width, height, label="button", color=(255,255,255), onClick=None):
        self.id = id
        super().__init__(x, y, width, height)
        self.label = label
        self.color = color
        self.onClick = onClick
        self.button = shapes.Rectangle(
            self.x, 
            self.y, 
            self.width, 
            self.height, 
            color=self.color
        )
        self.textLabel = text.Label(
            self.label,
            font_name='Arial',
            font_size=18,
            x=self.x + self.width / 2,
            y=self.y + self.height / 2,
            anchor_x='center',
            anchor_y='center'
        )

    def draw(self):
        if not self.visible:
            return
        self.button.draw()
        self.textLabel.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        onButton = (self.x <= x <= self.x + self.width and 
                    self.y <= y <= self.y + self.height)

        if onButton:
            if self.onClick:
                self.onClick()
    