from client.gui.GuiScreen import GuiScreen
from client.gui.GuiButton import GuiButton

from client.gui.screens.GuiOptions import GuiOptions
from client.gui.screens.GuiInGame import GuiInGame

class GuiMainMenu(GuiScreen):
    GUI_NAME = "MAIN MENU"

    def __init__(self, game):
        super().__init__(game)
        self.backgroundColor = (1.0, 0.0, 1.0, 1.0)
        self.setTitle(self.GUI_NAME)

        buttons = [
            ("New game", self.startGame),
            ("Load game", self.startGame),
            ("OPTIONS", self.openOptions),
            ("EXIT", self.game.close_game)
        ]

        buttonWidth = 400
        buttonHeight = 60
        spacing = 50
        buttonCount = len(buttons)

        totalHeight = (buttonHeight*buttonCount)+(spacing*(buttonCount-1))
        startY = (game.height + totalHeight)/2 - buttonHeight
        centerX = (game.width - buttonWidth) /2

        for i, (text, callback) in enumerate(buttons):
            y = startY - i*(buttonHeight+spacing)        
            button = GuiButton(
                id=i, 
                x=centerX, 
                y=y, 
                width=buttonWidth, 
                height=buttonHeight, 
                label=text,
                color=(0,154,157), 
                onClick=callback
            )
            self.add_widget(button)

    def startGame(self):
        self.game.displayGuiScreen(GuiInGame(self.game))

    def openOptions(self):
        self.game.displayGuiScreen(GuiOptions(self.game))
