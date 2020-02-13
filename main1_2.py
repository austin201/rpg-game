from RpgHero import *
from Armor1_2 import *
#
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
    player.equipAll()
    players.append(player)



turn = 0
notturn = 1
while players[0].alive:
    print()
    print("It's your attack")
    print(players[turn])
    x = players[turn].attack()
    players[notturn].defend(x)
    if players[1].alive:
        xp, item = players[1].die()
        players[0].addxp(xp)
        players[0].addToInv()
        players[0].equipAll()
        print("A new challenger approaches")
        time.sleep(3)
        player = Hero()
        players[1] = player

    turn, notturn = switchturns(turn)
print(players[0].name,"has died")
