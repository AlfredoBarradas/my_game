from game.entity.player.EntityPlayer import EntityPlayer as player

class Game():
    def __init__(self):
        self.name = "My Game"
        self.version = "0.01.01"
        self.active = True
        self.running = False
        self.currentScreen = None

    def run(self):
        self.running = True
        print(f"{self.name}, v{self.version}")
        self.main_loop()

    def is_Active(self):
        return self.active
    
    def is_running(self):
        return self.running

    def displayGuiScreen(self, screen):
        if not self.is_Active():
            print("Game is not active. Cannot display GUI screen.")
            return
        else:
            self.currentScreen = screen
            print(f"Displaying GUI screen: {screen}\n")

    def main_loop(self):
        if not self.is_running() and not self.is_Active():
            print("Game is not active. Cannot start.")
            return
        
        main_player = player("Player1")        
        while self.running and self.is_Active():
## ===================================================================

            self.displayGuiScreen("Main Menu")
            print(f"{main_player.name}, Tu vida actual es {main_player.getLife()}/{main_player.getMaxLife()}")

            useresponse = input("check:> ")
            if useresponse == "false":
                self.active = False
                print("Game is now inactive.")

            if useresponse == "1":
                main_player.atributes()

            if useresponse == "2":
                self.displayGuiScreen("Inventory")

            if useresponse == "3":
                self.displayGuiScreen("Crafting")
## ===================================================================

if __name__ == "__main__":
    game = Game()
    game.run()