from client.gui.GuiScreen import GuiScreen
from client.gui.GuiButton import GuiButton

class GuiMainMenu(GuiScreen):
    GUI_NAME = "Main Menu"
    def __init__(self):
        super().__init__()
        self.backgroundColor = (0.5, 0.5, 0.5, 1.0)
        #playButton = GuiButton(1, 20, 20, 100, 100, string="NEW GAME", color=(1,1,1))
        #self.add_widget(playButton)
