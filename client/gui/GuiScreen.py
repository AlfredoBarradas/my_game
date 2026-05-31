from client.gui.Gui import Gui

class GuiScreen(Gui):
    def __init__(self):
        super().__init__()
        self.widgets = []
        self.backgroundColor = (0.0, 0.0, 0.0, 1.0)

    def add_widget(self, widget):
        self.widgets.append(widget)

    def draw(self):
        for widget in self.widgets:
            widget.draw()

    def on_key_press(self, symbol, modifiers):
        for widget in self.widgets:
            widget.on_key_press(symbol, modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        for widget in self.widgets:
            widget.on_mouse_press(x, y, button, modifiers)