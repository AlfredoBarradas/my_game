from client.gui.GuiScreen import GuiScreen

class GuiInGame(GuiScreen):
    GUI_NAME = "In Game"
    def __init__(self, game):
        super().__init__(game)
        self.backgroundColor = (0.0, 1.0, 0.0, 1.0)
        self.setTitle(self.GUI_NAME)
