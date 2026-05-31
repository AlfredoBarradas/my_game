class Gui:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.xPos = x
        self.yPos = y
        self.width = width
        self.height = height

        self.visible = True
        self.enabled = True

    def update(self):
        pass

    def draw(self):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass