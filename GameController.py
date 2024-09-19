import random
class GameController:
    def __init__(self, fields, players):
        self.position = {}
        self.fields = fields
        self.players = players
        self.freq = {i: 0 for i in range(40)}

    def start(self):
        for i in range(1000000):
            for player in self.players:
                a, b = random.randint(1, 6), random.randint(1, 6)
                if player.jailed>0:
                    if a==b:
                        player.jailed = 0
                        self.move(player, player.position+a+b)
                    else:
                        player.jailed -= 1
                        if player.jailed == 0:
                            player.balance -= 50
                else:
                    self.move(player, player.position+a+b)
                    if a == b and player.jailed == 0:
                        a, b = random.randint(1, 6), random.randint(1, 6)
                        self.move(player, player.position + a + b)
                        if a == b and player.jailed == 0:
                            a, b = random.randint(1, 6), random.randint(1, 6)
                            self.move(player, player.position + a + b)
                            if a==b:
                                player.jailed = 3
                                self.move(player, 10)
        su = sum(self.freq.values())
        for k,v in self.freq.items():
            per = v/su*100
            print(f"{k} - {per:.2f}")


    def move(self, player, index):
        if index > 39:
            index -= 40
            player.balance += 200
        self.freq[index] += 1
        if index == 30:
            player.position = 10
            player.jailed = 3
        else:
            player.position = index
        #print(f"{player.name} - pos: {player.position} - balance {player.balance} - jailed: {player.jailed}")
