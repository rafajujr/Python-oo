class Game:
    # Método construtor
    def __init__(self, name="", yearLaunch=0, multiplayer=False, notes=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.notes = notes


    
game1 = Game("Minecraft", 2011, True, 4)
print(game1)
print(game1.name, game1.yearLaunch, game1.multiplayer, game1.notes)

    # def __init__(self):
    #     pass