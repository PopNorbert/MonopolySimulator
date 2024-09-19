from GameController import GameController
from Model.FIeld import Field
from Model.Player import Player

fields = [Field("shf")]
players = [Player("A"), Player("B"),Player("C"),Player("D")]
game = GameController(fields, players)
game.start()