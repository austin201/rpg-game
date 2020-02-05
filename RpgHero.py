from Armor1_2 import *
import random
import time

class Hero(object):
    racelist = ["Human", "Elf", "Dwarf", "Dog", ]
    classlist = ["Warrior", "Mage", "Hunter", "Dog"]
    def __init__(self):
        self.alive = True
        self.level = 1
        self.classe = self.pickclass()
        self.race = self.pickRace()
        self.name = self.enterName()

        self.xp = 0
        self.levelup = 90 + (self.level * 10)

        self.healthMod = 10
        self.maxhealth = self.level * self.healthMod
        self.healthAct = self.maxhealth

        self.manaMod = 10
        self.maxMana = self.level * self.manaMod
        self.manaAct = self.maxMana

        self.deff = 0
        self.atk = 0
        self.luck = 0
        self.stamina = 0
        self.iq = 0
        self.agi = 0
        self.atklist = []
        self.setMods()

        self.inventory = []
        self.maxInv = 10
        self.headeq = []
        self.chesteq = []
        self.legseq = []
        self.bootseq = []
        self.gloveseq = []
        self.rightHandeq = []
        self.leftHandeq = []
        self.popInv()
    def popInv(self):
        helm = Helm()
        chest = Chest()
        legs = Legs()
        boots = Boots()
        gloves = Gloves()
        x = random.randint(0, 7)
        if x == 0:
            weapon = Sword()
        elif x == 1:
            weapon = Bat()
        elif x == 2:
            weapon = Bow()
        elif x == 3:
            weapon = Stick()
        elif x == 4:
            weapon = Gun()
        elif x == 5:
            weapon = Mace()
        elif x == 6:
            weapon = Boomerang()
        else:
            weapon = Staf()
        self.addToInv(helm)
        self.addToInv(chest)
        self.addToInv(legs)
        self.addToInv(boots)
        self.addToInv(gloves)
        self.addToInv(weapon)
        x = random.randint(0, 3)
        for i in range(x):
            self.addToInv("Health Potion")
        x = random.randint(0, 3)
        for i in range(x):
            self.addToInv("Mana Potion")
    def addToInv(self, item):
        if len(self.inventory) < self.maxInv:
            self.inventory.append(item)
        else:
            print("You have to many items in your inventory.")
            return
    def pickRace(self):
        while True:
            try:
                print(Hero.racelist)
                x = input("Pick your Race: ").title()
                if x in Hero.racelist:
                    return x
            except:
                print("Not a good option")
    def pickclass(self):
        while True:
            try:
                print(Hero.classlist)
                x = input("Pick your Class: ").title()
                if x in Hero.classlist:
                    return x
            except:
                print("Not a good option")
    def enterName(self):
        name = ""
        while name == "":
            name = input("What would you like to name this character: ").title()
            x = name
            return x
    def setMods(self):
        if self.classe == "Warrior":
            self.atklist = ["sword stab", "shield bash", "sword flip"]
            self.deff = random.randint(5, 20)
            self.atk = random.randint(5, 15)
            self.luck = random.randint(1, 4)
            self.stamina = random.randint(10, 20)
            self.iq = 1
            self.agi = random.randint(1, 5)
            self.maxMana = 0
        if self.classe == "Mage":
            self.atklist = ["staff swipe", "staff shot", "fireball"]
            self.deff = random.randint(5, 15)
            self.atk = random.randint(10, 15)
            self.luck = random.randint(4, 7)
            self.stamina = random.randint(10, 20)
            self.iq = 1
            self.agi = random.randint(5, 10)
            self.maxMana = random.randint(1, 10)
        if self.classe == "Hunter":
            self.atklist = ["shot", "knife stab", "grenade"]
            self.deff = random.randint(5, 10)
            self.atk = random.randint(5, 25)
            self.luck = random.randint(1, 4)
            self.stamina = random.randint(15, 25)
            self.iq = 1
            self.agi = random.randint(1, 3)
            self.maxMana = random.randint(1, 10)
        if self.classe == "Dog":
            self.atklist = ["bite", "jump bite", "bark"]
            self.deff = random.randint(10, 20)
            self.atk = random.randint(20, 25)
            self.luck = random.randint(5, 10)
            self.stamina = random.randint(15, 25)
            self.iq = 1
            self.agi = random.randint(5, 10)
            self.maxMana = random.randint(1, 10)
        if self.race == "Elf":
            self.stamina -= 3
            self.iq += 2
        if self.race == "Human":
            self.stamina += 3
            self.iq += 3
            self.luck += 3
        if self.race == "Dwarf":
            self.stamina += 2
            self.iq -= 2
        if self.race == "Dog":
            self.atk += 10
            self.deff += 10
            self.luck += 10
            self.stamina += 5
            self.iq += 10
            self.agi += 10
    def die(self, winner):
        dropxp = 10 * self.level
        print(dropxp)
        # winner.givexp(dropxp)
        item = random.choice(self.inventory)
        print(item)
        # winner.giveitem(item)
    def addxp(self, xp):
        print("Picked up" + )
    def __str__(self):
        return """
       Name: {}  \tRace: {}\tClass: {}  \tLevel: {}
       Health: {}
       Attack: {}
       Defence: {}
       Luck: {}
       Stamina: {}
       IQ: {}
       Agility: {}
       XP: {}
       Mana: {}""".format(self.name, self.race, self.classe, self.level, self.healthAct, self.atk, self.deff, self.luck,
                        self.stamina, self.iq, self.agi, self.xp,self.manaAct)
    def levelUp(self):
        if self.xp >= self.levelup:
            self.level += 1
            remaingxp = self.xp - self.levelup
            self.xp = remaingxp
            self.levelup = 90 + (self.level * 10)
            self.healthMod += self.level
            self.maxhealth = self.level * self.healthMod
            self.healthAct = self.maxhealth
            if self.classe != "Warrior":
                self.manaMod += self.level
                self.maxMana = self.level * self.manaMod
                self.manaAct = self.maxMana
    def equipGloves(self):
        for i in self.inventory:
            x = type(i)
            if "Gloves" in str(x):
                if len(self.gloveseq) < 1:
                    print("You equipped a set of gloves")
                    print(i)
                    self.gloveseq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.gloveseq[0].armor
                    self.luck += self.gloveseq[0].luck
                    self.stamina += self.gloveseq[0].stamina
                    self.iq += self.gloveseq[0].iq
                    self.agi += self.gloveseq[0].agi
                else:
                    print("You need to remove your equipped gloves first.")
                    print("You are wearing a pair of gloves.")
                    print(self.gloveseq[0])
                    print("Would you like to replace them with.")
                    print(i)
                    while True:
                        x = input("yes or no: ")
                        if x == "yes":
                            print("You replaced your gloves.")
                            self.deff -= self.gloveseq[0].armor
                            self.luck -= self.gloveseq[0].luck
                            self.stamina -= self.gloveseq[0].stamina
                            self.iq -= self.gloveseq[0].iq
                            self.agi -= self.gloveseq[0].agi
                            self.gloveseq.remove(self.gloveseq[0])
                            self.gloveseq.append(i)
                            self.inventory.remove(i)
                            self.gloveseq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.gloveseq[0].armor
                            self.luck += self.gloveseq[0].luck
                            self.stamina += self.gloveseq[0].stamina
                            self.iq += self.gloveseq[0].iq
                            self.agi += self.gloveseq[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break
    def equipHelm(self):
        for i in self.inventory:
            x = type(i)
            if "Helm" in str(x):
                if len(self.headeq) < 1:
                    print("You equipped a helmet")
                    print(i)
                    self.headeq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.headeq[0].armor
                    self.luck += self.headeq[0].luck
                    self.stamina += self.headeq[0].stamina
                    self.iq += self.headeq[0].iq
                    self.agi += self.headeq[0].agi
                else:
                    print("You need to remove your equipped helmet first.")
                    print("You are wearing a helmet.")
                    print(self.headeq[0])
                    print("Would you like to replace them with.")
                    print(i)
                    while True:
                        x = input("yes or no: ")
                        if x == "yes":
                            print("You replaced your helmet.")
                            self.deff -= self.headeq[0].armor
                            self.luck -= self.headeq[0].luck
                            self.stamina -= self.headeq[0].stamina
                            self.iq -= self.headeq[0].iq
                            self.agi -= self.headeq[0].agi
                            self.headeq.remove(self.headeq[0])
                            self.headeq.append(i)
                            self.inventory.remove(i)
                            self.headeq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.headeq[0].armor
                            self.luck += self.headeq[0].luck
                            self.stamina += self.headeq[0].stamina
                            self.iq += self.headeq[0].iq
                            self.agi += self.headeq[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break
    def equipChest(self):
        for i in self.inventory:
            x = type(i)
            if "Chest" in str(x):
                if len(self.chesteq) < 1:
                    print("You equipped a chestplate")
                    print(i)
                    self.chesteq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.chesteq[0].armor
                    self.luck += self.chesteq[0].luck
                    self.stamina += self.chesteq[0].stamina
                    self.iq += self.chesteq[0].iq
                    self.agi += self.chesteq[0].agi
                else:
                    print("You need to remove your equipped chestplate first.")
                    print("You are wearing a chestplate.")
                    print(self.chesteq[0])
                    print("Would you like to replace them with.")
                    print(i)
                    while True:
                        x = input("yes or no: ")
                        if x == "yes":
                            print("You replaced your chestplate.")
                            self.deff -= self.chesteq[0].armor
                            self.luck -= self.chesteq[0].luck
                            self.stamina -= self.chesteq[0].stamina
                            self.iq -= self.chesteq[0].iq
                            self.agi -= self.chesteq[0].agi
                            self.chesteq.remove(self.chesteq[0])
                            self.chesteq.append(i)
                            self.inventory.remove(i)
                            self.chesteq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.chesteq[0].armor
                            self.luck += self.chesteq[0].luck
                            self.stamina += self.chesteq[0].stamina
                            self.iq += self.chesteq[0].iq
                            self.agi += self.chesteq[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break
    def equipLegs(self):
        for i in self.inventory:
            x = type(i)
            if "Legs" in str(x):
                if len(self.legseq) < 1:
                    print("You equipped pants")
                    print(i)
                    self.legseq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.legseq[0].armor
                    self.luck += self.legseq[0].luck
                    self.stamina += self.legseq[0].stamina
                    self.iq += self.legseq[0].iq
                    self.agi += self.legseq[0].agi
                else:
                    print("You need to remove your equipped pants first.")
                    print("You are wearing a pants.")
                    print(self.legseq[0])
                    print("Would you like to replace them with.")
                    print(i)
                    while True:
                        x = input("yes or no: ")
                        if x == "yes":
                            print("You replaced your pants.")
                            self.deff -= self.legseq[0].armor
                            self.luck -= self.legseq[0].luck
                            self.stamina -= self.legseq[0].stamina
                            self.iq -= self.legseq[0].iq
                            self.agi -= self.legseq[0].agi
                            self.legseq.remove(self.legseq[0])
                            self.legseq.append(i)
                            self.inventory.remove(i)
                            self.legseq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.legseq[0].armor
                            self.luck += self.legseq[0].luck
                            self.stamina += self.legseq[0].stamina
                            self.iq += self.legseq[0].iq
                            self.agi += self.legseq[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break
    def equipBoots(self):
        for i in self.inventory:
            x = type(i)
            if "Boots" in str(x):
                if len(self.bootseq) < 1:
                    print("You equipped boots")
                    print(i)
                    self.bootseq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.bootseq[0].armor
                    self.luck += self.bootseq[0].luck
                    self.stamina += self.bootseq[0].stamina
                    self.iq += self.bootseq[0].iq
                    self.agi += self.bootseq[0].agi
                else:
                    print("You need to remove your equipped boots first.")
                    print("You are wearing a boots.")
                    print(self.bootseq[0])
                    print("Would you like to replace them with.")
                    print(i)
                    while True:
                        x = input("yes or no: ")
                        if x == "yes":
                            print("You replaced your boots.")
                            self.deff -= self.bootseq[0].armor
                            self.luck -= self.bootseq[0].luck
                            self.stamina -= self.bootseq[0].stamina
                            self.iq -= self.bootseq[0].iq
                            self.agi -= self.bootseq[0].agi
                            self.bootseq.remove(self.bootseq[0])
                            self.bootseq.append(i)
                            self.inventory.remove(i)
                            self.bootseq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.bootseq[0].armor
                            self.luck += self.bootseq[0].luck
                            self.stamina += self.bootseq[0].stamina
                            self.iq += self.bootseq[0].iq
                            self.agi += self.bootseq[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break
    def equipWeapon(self):
        for i in self.inventory:
            x = type(i)
            if ("Sword" in str(x) or "Gun" in str(x) or "Bow" in str(x) or "Bat" in str(x) or "Mace" in str(x) or "Stick" in str(x) or "Staf" in str(x) or "Boomerang" in str(x)):
            # if i.eqType == "Weapon":
                while True:
                    x = input("""Would you like to equip the weapon in your right or left hand(right or left).
""")
                    if x == "right":
                        if len(self.rightHandeq) < 1:
                            print("You equipped a weapon in your right hand.")
                            print(i)
                            self.rightHandeq.append(i)
                            self.inventory.remove(i)
                            self.atk += self.rightHandeq[0].damage
                            self.luck += self.rightHandeq[0].luck
                            self.stamina += self.rightHandeq[0].stamina
                            self.iq += self.rightHandeq[0].iq
                            self.agi += self.rightHandeq[0].agi
                            break
                        else:
                            print("You already have a weapon in that hand.")
                            print(self.rightHandeq[0])
                            print("Would you like to replace it with")
                            print(i)
                            while True:
                                x = input("yes or no: ")
                                if x == "yes":
                                    print("You replaced your right hand weapon.")
                                    self.atk -= self.rightHandeq[0].damage
                                    self.luck -= self.rightHandeq[0].luck
                                    self.stamina -= self.rightHandeq[0].stamina
                                    self.iq -= self.rightHandeq[0].iq
                                    self.agi -= self.rightHandeq[0].agi
                                    self.rightHandeq.remove(self.rightHandeq[0])
                                    self.rightHandeq.append(i)
                                    self.inventory.remove(i)
                                    self.atk += self.rightHandeq[0].damage
                                    self.luck += self.rightHandeq[0].luck
                                    self.stamina += self.rightHandeq[0].stamina
                                    self.iq += self.rightHandeq[0].iq
                                    self.agi += self.rightHandeq[0].agi
                                    break
                                if x == "no":
                                    self.inventory.remove(i)
                                    break
                    elif x == "left":
                        if len(self.leftHandeq) < 1:
                            print("You equipped a weapon in your left hand.")
                            print(i)
                            self.leftHandeq.append(i)
                            self.inventory.remove(i)
                            self.atk += self.leftHandeq[0].damage
                            self.luck += self.leftHandeq[0].luck
                            self.stamina += self.leftHandeq[0].stamina
                            self.iq += self.leftHandeq[0].iq
                            self.agi += self.leftHandeq[0].agi
                            break
                        else:
                            print("You already have a weapon in that hand.")
                            print(self.leftHandeq[0])
                            print("Would you like to replace it with")
                            print(i)
                            while True:
                                x = input("yes or no: ")
                                if x == "yes":
                                    print("You replaced your left hand weapon.")
                                    self.atk -= self.leftHandeq[0].damage
                                    self.luck -= self.leftHandeq[0].luck
                                    self.stamina -= self.leftHandeq[0].stamina
                                    self.iq -= self.leftHandeq[0].iq
                                    self.agi -= self.leftHandeq[0].agi
                                    self.leftHandeq.remove(self.leftHandeq[0])
                                    self.leftHandeq.append(i)
                                    self.inventory.remove(i)
                                    self.atk += self.leftHandeq[0].damage
                                    self.luck += self.leftHandeq[0].luck
                                    self.stamina += self.leftHandeq[0].stamina
                                    self.iq += self.leftHandeq[0].iq
                                    self.agi += self.leftHandeq[0].agi
                                    break
                                if x == "no":
                                    self.inventory.remove(i)
                                    break
                    else:
                        print("Not an option")
    def equipAll(self):
        self.equipHelm()
        time.sleep(10)
        self.equipChest()
        time.sleep(10)
        self.equipGloves()
        time.sleep(10)
        self.equipLegs()
        time.sleep(10)
        self.equipBoots()
        time.sleep(10)
        self.equipWeapon()
    def useHpPotion(self):
        for i in self.inventory:
            if i == "Health potion":
                self.healthAct = self.maxhealth
                self.inventory.remove(i)
                return
    def useMpPotion(self):
        for i in self.inventory:
            if i == "Mana potion":
                self.manaAct = self.maxMana
                self.inventory.remove(i)
                return
    def attack(self):
        #attack = input("""How strong do you want your attack.(strong, weak, medium)""").lower()
        miss = 5
        if self.iq > 100:
            miss = 10
        if self.iq > 150:
            miss = 13
        if self.iq > 200:
            miss = 16
        roll = random.randint(1,miss)
        if roll == 1:
            print(self.name,"Missed")
            return 0
        roll = random.randint(1, 12)
        if self.classe == "Warrior":
            for i in range(len(self.atklist)):
                print(i + 1, self.atklist[i])
            while True:
                x = input("""What attack would you like to use 1,2,3,or 4 to use a health potion.
    1 = Weak Attack
    2 = Medium Attack
    3 = Strong Attack
    4 = Health Potion
""")
                if x == "1":
                    attk = ((self.atk + self.stamina) * roll) * .1
                    break
                elif x == "2" and self.stamina > 10:
                    attk = ((self.atk + self.stamina) * roll) * .2
                    self.stamina -=10
                    break
                elif x == "3" and self.stamina > 20:
                    attk = ((self.atk + self.stamina) * roll) * .3
                    self.stamina -=20
                    break
                elif x == "4":
                    self.useHpPotion()
                    attk = 0
                    break
                else:
                    print("Not an option")
        elif self.classe == "Mage":
            for i in range(len(self.atklist)):
                print(i + 1, self.atklist[i])
            while True:
                x = input("""What attack would you like to use 1,2,3,4, or 5 to use a health potion.
    1 = Weak Attack
    2 = Medium Attack
    3 = Strong Attack
    4 = Health Potion
    5 = Mana Potion.
""")
                if x == "1" and self.manaAct > 1:
                    attk = ((self.atk + self.iq) * roll) * .1
                    self.manaAct -=1
                    break
                elif x == "2" and self.manaAct > 3:
                    attk = ((self.atk + self.iq) * roll) * .2
                    self.manaAct -=3
                    break
                elif x == "3" and self.manaAct > 5:
                    attk = ((self.atk + self.iq) * roll) * .3
                    self.manaAct -=5
                    break
                elif x == "4":
                    self.useHpPotion()
                    attk = 0
                    break
                elif x == "5":
                    self.useMpPotion()
                    attk = 0
                    break
                else:
                    print("Not an option")
        elif self.classe == "Hunter":
            for i in range(len(self.atklist)):
                print(i + 1, self.atklist[i])
            while True:
                x = input("""What attack would you like to use 1,2,3,4, or 5 to use a health potion.
    1 = Weak Attack
    2 = Medium Attack
    3 = Strong Attack
    4 = Health Potion
    5 = Mana Potion.
""")
                if x == "1" and self.manaAct > 1:
                    attk = ((self.atk + self.agi) * roll) * .1
                    self.manaAct -= 1
                    break
                elif x == "2" and self.manaAct > 3:
                    attk = ((self.atk + self.agi) * roll) * .2
                    self.manaAct -= 3
                    break
                elif x == "3" and self.manaAct > 5:
                    attk = ((self.atk + self.agi) * roll) * .3
                    self.manaAct -= 5
                    break
                elif x == "4":
                    self.useHpPotion()
                    attk = 0
                    break
                elif x == "5":
                    self.useMpPotion()
                    attk = 0
                    break
                else:
                    print("Not an option")
        elif self.classe == "Dog":
            for i in range(len(self.atklist)):
                print(i + 1, self.atklist[i])
            while True:
                x = input("""What attack would you like to use 1,2,3,4, or 5 to use a health potion.
    1 = Weak Attack
    2 = Medium Attack
    3 = Strong Attack
    4 = Health Potion
    5 = Mana Potion.
""")
                if x == "1" and self.manaAct > 1:
                    attk = ((self.atk + self.luck) * roll) * .1
                    self.manaAct -= 1
                    break
                elif x == "2" and self.manaAct > 3:
                    attk = ((self.atk + self.luck) * roll) * .2
                    self.manaAct -= 3
                    break
                elif x == "3" and self.manaAct > 5:
                    attk = ((self.atk + self.luck) * roll) * .3
                    self.manaAct -= 5
                    break
                elif x == "4":
                    self.useHpPotion()
                    attk = 0
                    break
                elif x == "5":
                    self.useMpPotion()
                    attk = 0
                    break
                else:
                    print("Not an option")
        crit = 20
        if self.luck > 100:
            crit = 15
        elif self.luck > 150:
            crit = 10
        roll = random.randint(1,crit)
        if roll == 7:
            attk = attk*3
        print(self.name, "did", attk, "damage")
        return attk
    def defend(self, damage):
        blc = 20
        dmg = damage
        if self.iq > 100:
            blc = 15
        if self.iq > 150:
            blc = 10
        if self.iq > 200:
            blc = 5
        roll = random.randint(1,blc)
        if roll == 5:
            print("Block")
            dmg = 0
        roll = random.randint(1,6)
        if self.classe == "Warrior":
            block = ((self.deff + self.agi)*roll)*.1
        elif self.classe == "Mage":
            block = ((self.deff + self.luck) * roll) * .1
        elif self.classe == "Hunter":
            block = ((self.deff + self.stamina) * roll) * .1
        else:
            block = ((self.deff + self.iq) * roll) * .1
        print(self.name, "blocked", block, "damage")
        dmgdelt = dmg - block
        if dmgdelt >= 0:
            self.healthAct = self.healthAct - dmgdelt
        if self.healthAct <= 0:
            self.alive = False