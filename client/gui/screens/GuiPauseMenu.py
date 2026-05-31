from client.gui.GuiScreen import GuiScreen
from client.gui.GuiButton import GuiButton

from client.gui.screens.GuiOptions import GuiOptions
from client.gui.screens.GuiInGame import GuiInGame
from client.gui.screens.GuiMainMenu import GuiMainMenu


class GuiPauseMenu(GuiScreen):
    GUI_NAME = "PAUSE"

    def __init__(self, game):
        super().__init__(game)
        self.backgroundColor = (0.0, 0.0, 0.0, 0.1)
        self.setTitle(self.GUI_NAME)

        buttonWidth = 400
        buttonHeight = 60
        spacing = 50
        buttonCount = 3

        totalHeight = (buttonHeight*buttonCount)+(spacing*(buttonCount-1))
        startY = (game.height + totalHeight)/2 - buttonHeight
        centerX = (game.width - buttonWidth) /2

        for i in range(buttonCount):
            y = startY - i*(buttonHeight+spacing)        
            button = GuiButton(
                i, 
                x=centerX, 
                y=y, 
                width=buttonWidth, 
                height=buttonHeight, 
                color=(0,154,157), 
                onClick=lambda i=i: self.buttonClicked(i)
            )
            self.add_widget(button)

    def buttonClicked(self, buttonId):
        if buttonId == 0:
            print("Resume")
            self.game.displayGuiScreen(GuiInGame(self.game))

        elif buttonId == 1:
            print("Options")
            self.game.displayGuiScreen(GuiOptions(self.game))

        elif buttonId == 2:
            print("Return to Main Menu")
            self.game.displayGuiScreen(GuiMainMenu(self.game))
