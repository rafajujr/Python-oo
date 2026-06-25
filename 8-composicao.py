# Classe Pai (Super classe) - Generalista
class Game:
    total_games = 0 # Variável de classe
    # - Método construtor
    def __init__(self, nome, yearLaunch, multiplayer, notes):
        self.nome = nome
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.notes = notes
        Game.total_games += 1
        self.totalEvaluate = 0
        self.evaluators = 0

    # - Método str
    def __str__(self):
        return f"Nome: {self.nome} - Ano de Lançamento: {self.yearLaunch} - Multiplayer: {self.multiplayer} - Notas: {self.notes}"
    
    # - Método instancia
    def technical_sheet(self):
        print("#### Nome do Jogo ###")
        print(self.nome)
        print("#### Ano de Lançamento ###")
        print(self.yearLaunch)
        print("#### Multiplayer ###")
        print(self.multiplayer)
        print("#### Notas ###")
        print(self.notes)
        print("####################\n")

class GameStdio:
    def __init__(self, name=""):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def evaluate_studio_quality(self):
        total_notes = sum(game.notes for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estúdio {self.name} ainda nao criou nenhum jogo.")
        else:
            average_note = total_notes / num_games
            print(f"A nota média do estúdio {self.name} é: {average_note}")

#Exemplos de games
game1 = Game("Minecraft", 2011, True, 4)
game2 = Game("Fortnite", 2017, True, 5)
game3 = Game("Tetris", 1984, False, 5)
game4 = Game("Avatar", 2009, True, 4)
studio1 = GameStdio("Studio 1")
studio1.add_game(game1)
studio1.add_game(game2)
studio1.add_game(game3)
studio1.add_game(game4)
studio1.evaluate_studio_quality()

for game in studio1.games:
    game.technical_sheet()