from RpgHero import *
from Armor1_2 import *
import time
def switchturns(turn):
    if turn == 0:
        turn = 1
        notturn = 0
    else:
        turn = 0
        notturn = 1
    return turn, notturn

players = []

for i in range(2):
    print("Create player", i + 1)
    player = Hero()
    player.popInv()
    players.append(player)

for i in players:

turn = 0
notturn = 1
while players[0].alive:
    x = players[turn].attack()
    players[notturn].defend(x)
    if players[1].alive:
        xp, item = players[1].die()
        player = Hero()
        players[1] = player
    players[turn].addxp(xp)
    players[turn].addToInv(item)
    turn, notturn = switchturns(turn)

