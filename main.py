print("base code")

def main_loop():
    print("main code")

    def entity(name, life) -> dict:
        return {
            "name": name, 
            "life": life
        }
    
    player = entity("player", 100)

    while player["life"] > 0:
        print(f"{player['name']} has {player['life']} life left.")
        damage = int(input(f"Enter damage taken: >\n"))
        player["life"] -= damage

        if  player["life"] <= 0:
            print(f"{player['name']} has died.")
            break

    print("Game Over")
    restart = input("Do you want to restart? (y/n) >\n")
    if restart.lower() == "y":
        main_loop()
    else:
        print("Thanks for playing!")
if __name__ == "__main__":
    main_loop()