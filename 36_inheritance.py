class player:
    def __init__(self, name):
        self.name = name
        self.is_retired = True

    def play(self):
        print(f"{self.name} is playing")

    def sleep(self):
        print("zzz...")

class player1(player):
    pass

class player2(player):
    pass

Player1=player1("Messi")
Player2=player2("Ronaldo")

print(Player1.name)

Player2.play()
    