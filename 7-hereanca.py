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

    # - Método instancia
    def evaluate(self, note):
        self.totalEvaluate += note
        self.evaluators += 1

    # - Método instancia
    def avarage(self):
        return f"A nota média de avaliação do Game {self.nome} é: {self.totalEvaluate / self.evaluators}"

# Classe derivada (Subclasse) - Especializada
class SinglePLayerGame(Game):
    def __init__(self, nome="", yearLaunch=0, notes=0, storyline=""):
        super().__init__(nome, yearLaunch, multiplayer=False, notes=notes)
        self.storyline = storyline

    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyline}\n")

mult_game = Game("Fortnite", 2017, True, 5)
single_game = SinglePLayerGame("Avatar", 2009, 4, "Aventura no futuro em um mundo de fantasia")
mult_game.technical_sheet()
single_game.technical_sheet()