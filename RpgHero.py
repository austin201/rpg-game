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
        self.alive = False
        dropxp = 10 * self.level
        print(dropxp)
        # winner.givexp(dropxp)
        item = random.choice(self.inventory)
        print(item)
        # winner.giveitem(item)
    def mageattk(self):
        attacking = input("""Do you want to do a strong attack, magic attack, or weak attack.""").lower()
    def attack(self):
        attacks = input(
            """Do you want to do a strong attack, medium attack, or weak attack. Just type the first word before attack.""").lower()
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
       XP: {}""".format(self.name, self.race, self.classe, self.level, self.healthAct, self.atk, self.deff, self.luck,
                        self.stamina, self.iq, self.agi, self.xp)
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
                        x = input("yes or no")
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
                        x = input("yes or no")
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
                        x = input("yes or no")
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
                        x = input("yes or no")
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
                        x = input("yes or no")
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
                    x = input("Would you like to equip the weapon in your right or left hand(right or left).")
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
                                x = input("yes or no")
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
                                x = input("yes or no")
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
        time.sleep(5)
        self.equipChest()
        time.sleep(5)
        self.equipGloves()
        time.sleep(5)
        self.equipLegs()
        time.sleep(5)
        self.equipBoots()
        time.sleep(5)
        self.equipWeapon()

