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

game1 = Game("Minecraft", 2011, True, 4)
game2 = Game("Fortnite", 2017, True, 5)
game1.technical_sheet()
game2.technical_sheet()
game1.evaluate(5)
game1.evaluate(6)
game2.evaluate(8)
game2.evaluate(9)
print(game1.avarage())
print(game2.avarage())

# Exibir o numero de jogos criados
print(f"Total de jogos criados: {Game.total_games}")