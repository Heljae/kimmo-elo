class Database:
    def __init__(self):
        self.palyers = {}

    def add_player(self):
        name = input("name: ")
        elo = 1500
        total_games = 0
        total_cups = 0

        self.palyers[name] = [elo, total_games, total_cups]

    def update_elo(self, elo):
        name = input("name: ")

        self.palyers[name] = elo

    def find_player_elo(self, name):
        return self.palyers[name]

class Player:
    def __init__(self, name, elo):
        self.name = name
        self.elo = elo