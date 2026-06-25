class Game:
    nome = ""
    yearLaunch = 0
    multiplayer = False
    notes = 0
    
# Primeio Jogo
game1 = Game()
game1.nome = "Minecraft"
game1.yearLaunch = 2011
game1.multiplayer = True
game1.notes = 4

# Segundo Jogo
game2 = Game()
game2.nome = "Fortnite"
game2.yearLaunch = 2017
game2.multiplayer = True
game2.notes = 5

# Terceiro Jogo
game3 = Game()
game3.nome = "Tetris"
game3.yearLaunch = 1984
game3.multiplayer = False
game3.notes = 5

# Quarto Jogo
game4 = Game()
game4.nome = "Avatar"
game4.yearLaunch = 2009
game4.multiplayer = True
game4.notes = 4

print("### Dados do Jogo ####")
print(f"Nome do jogo: {game1.nome}\n Ano de Lançamento: {game1.yearLaunch}\n Multiplayer: {game1.multiplayer}\n Avaliação: {game1.notes}")