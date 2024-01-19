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
            opponent_elo = float(input("opponent average elo: "))
            cups = int(input("cups you drank: "))
            new = input("first game (y/n) ")

            if new == "y":
                count = Elo(elo, opponent_elo, cups, True)
            else:
                count = Elo(elo, opponent_elo, cups, False)

            new_elo = count.count()

            self.db.palyers[name] = new_elo
            
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