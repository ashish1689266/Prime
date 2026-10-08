# Create a class player with:
# a class variable player_count
# instance variables name and level
# Track how many players were created.

class player:
    player_count = 0
    def __init__(self, name, level):
        self.name = name
        self.level = level
        # player.player_count += 1 "this will also work"
        player.count_player()

    @classmethod
    def count_player(cls):
        cls.player_count += 1

    def show_count(self):
        print(player.player_count)

player1 = player("Ashish", 8)
player1.show_count()
player2 = player("Rohit", 8)
player2.show_count()

print(f"Total no. of players is: {player.player_count}")