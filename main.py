from client.gui.screens.GuiMainMenu import GuiMainMenu

from pyglet import gl
from pyglet import app, window
from pyglet.window import key

class Game():
    GAME_NAME = "My Game"
    def __init__(self, width, height):
        self.name = self.GAME_NAME
        self.version = "0.01.01"

        self.width = width
        self.height = height

        self.active = True
        self.running = False
        self.loaded = False

        self.currentScreen = None

        self.window = window.Window(width=self.width, height=self.height, caption=self.name)
        self.window.push_handlers(self)

    def is_Active(self):
        return self.active
    
    def is_running(self):
        return self.running

    def displayGuiScreen(self, screen):
        if not self.is_Active():
            return
        self.currentScreen = screen

    def on_draw(self):
        if self.currentScreen is None:
            return
        gl.glClearColor(*self.currentScreen.backgroundColor)
        self.window.clear()
        self.currentScreen.draw()
        
    def on_key_press(self, symbol, modifiers):
        if self.currentScreen:
            self.currentScreen.on_key_press(symbol, modifiers)

        if symbol == key.ESCAPE:
            self.window.close()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.currentScreen:
            self.currentScreen.on_mouse_press(x, y, button, modifiers)
    
    def run(self):
        self.running = True
        print(f"{self.name}, v{self.version}")
        self.displayGuiScreen(GuiMainMenu())
        app.run()


if __name__ == "__main__":
    game = Game(800, 600)
    game.run()