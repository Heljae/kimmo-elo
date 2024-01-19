from elo import Elo
from db import Database

class Main():
    def __init__(self):
        self.db = Database()

    def commands(self):
        print()
        print("1 - add a player")
        print("2 - count elo")
        print("3 - print elos")
        print("0 - quit")
        print()

    def give_command(self, command):
        if command == 1:
            self.db.add_player()
        if command == 2:
            name = input("name: ")
            elo = float(self.db.find_player_elo(name))
            total_cups = int(input("number of cups in game:"))
            opponent_elo = float(input("opponent average elo: "))
            cups_drank = int(input("cups you drank: "))
            new = input("first game (y/n) ")

            if new == "y":
                count = Elo(elo, opponent_elo, cups_drank, True, total_cups)
            else:
                count = Elo(elo, opponent_elo, cups_drank, False, total_cups)

            new_elo = count.count()
            total_games = self.db.palyers[name][1] + 1
            total_cups = self.db.palyers[name][1] + cups_drank
            self.db.palyers[name] = [elo, total_games, total_cups]
            
            return new_elo
        if command == 3:
            print(self.db.palyers)
    
if __name__=="__main__":
    main = Main()
    while True:
        main.commands()
        command = int(input("command: "))
        print()
        if command == 0:
            print("bye")
            break
        else:
            main.give_command(command)