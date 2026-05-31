from client.gui.Gui import Gui

from pyglet import text

class GuiScreen(Gui):
    def __init__(self, game):
        super().__init__()
        self.game = game
        
        self.widgets = []
        self.backgroundColor = (0.0, 0.0, 0.0, 1.0)

        self.titleScreen = None

    def setTitle(self, title, fontSize=36):
        self.titleLabel = text.Label(
            title,
            font_name='Arial',
            font_size=fontSize,
            x=self.game.width / 2,
            y=self.game.height - 80,
            anchor_x='center',
            anchor_y='center'
        )


    def add_widget(self, widget):
        self.widgets.append(widget)

    def update(self, dt):
        for widget in self.widgets:
            widget.update(dt)

    def draw(self):
        if self.titleLabel:
            self.titleLabel.draw()
        for widget in self.widgets:
            widget.draw()

    def on_key_press(self, symbol, modifiers):
        for widget in self.widgets:
            widget.on_key_press(symbol, modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        for widget in self.widgets:
            widget.on_mouse_press(x, y, button, modifiers)
