import random
#

class Equipment(object):
    RARITY = ["Garbage","Useless","Better","Great","Amazing"]
    def __init__(self,eqType):
        self.raritylevel, self.rareMod = self.pickrare()
        self.eqtype = eqType


    def pickrare(self):
        x = random.randint(1, 10)
        if x >= 1 and x <= 2:
           return Equipment.RARITY[0], 2
        elif x > 2 and x <= 5:
           return Equipment.RARITY[1], 4
        elif x > 5 and x <= 8:
            return Equipment.RARITY[2], 6
        elif x > 8 and x < 9:
            return Equipment.RARITY[3], 8
        else:
            return Equipment.RARITY[4], 10


class Armor(Equipment):
    ARMORTYPE = ["Helm", "Chest", "Legs", "Boots", "Gloves"]

    def __init__(self, atype):
        super(Armor, self).__init__("Armor")
        self.armortype = atype
        self.armor = 0
        self.stamina = 0
        self.agi = 0
        self.iq = 0
        self.luck = 0

    def __str__(self):
        return """
            armorType: {}
            Rarity Level: {}
            Armor: {}
            Luck: {}
            Stamina: {}
            IQ: {}
            Agility: {}
            """.format(self.armortype, self.raritylevel, self.armor, self.luck, self.stamina, self.iq, self.agi)


class Helm(Armor):
    def __init__(self):
        super(Helm, self).__init__(Armor.ARMORTYPE[0])
        self.armor = random.randint(5, 10) * self.rareMod
        self.stamina = random.randint(0, 8) + self.rareMod
        self.agi = random.randint(0, 8) + self.rareMod
        self.iq = random.randint(0, 8) + self.rareMod
        self.luck = random.randint(0, 8) + self.rareMod


class Chest(Armor):
    def __init__(self):
        super(Chest, self).__init__(Armor.ARMORTYPE[1])
        self.armor = random.randint(7, 10) * self.rareMod
        self.stamina = random.randint(0, 5) + self.rareMod
        self.agi = random.randint(0, 5) + self.rareMod
        self.iq = random.randint(0, 9) + self.rareMod
        self.luck = random.randint(0, 4) + self.rareMod


class Legs(Armor):
    def __init__(self):
        super(Legs, self).__init__(Armor.ARMORTYPE[2])
        self.armor = random.randint(4, 7) * self.rareMod
        self.stamina = random.randint(0, 6) + self.rareMod
        self.agi = random.randint(0, 5) + self.rareMod
        self.iq = random.randint(0, 7) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod


class Boots(Armor):
    def __init__(self):
        super(Boots, self).__init__(Armor.ARMORTYPE[3])
        self.armor = random.randint(2, 5) * self.rareMod
        self.stamina = random.randint(5, 10) + self.rareMod
        self.agi = random.randint(5, 10) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 10) + self.rareMod


class Gloves(Armor):
    def __init__(self):
        super(Gloves, self).__init__(Armor.ARMORTYPE[4])
        self.armor = random.randint(3, 6) * self.rareMod
        self.stamina = random.randint(5, 10) + self.rareMod
        self.agi = random.randint(5, 10) + self.rareMod
        self.iq = random.randint(0, 7) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod


class Weapon(Equipment):
    WEAPONTYPE = ["Sword", "Bat", "Mace", "Stick", "Gun", "Bow", "Staf", "Boomerang"]

    def __init__(self, wtype):
        super(Weapon, self).__init__("Weapon")

        self.weapontype = wtype
        self.damage = 0
        self.stamina = 0
        self.agi = 0
        self.iq = 0
        self.luck = 0

    def __str__(self):
        return """
            weaponType: {}
            Rarity Level: {}
            Damage: {}
            Luck: {}
            Stamina: {}
            IQ: {}
            Agility: {}
            """.format(self.weapontype, self.raritylevel, self.damage, self.luck, self.stamina, self.iq, self.agi)


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__(Weapon.WEAPONTYPE[0])
        self.damage = random.randint(5, 10) * self.rareMod
        self.stamina = random.randint(2, 7) + self.rareMod
        self.agi = random.randint(2, 7) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 6) + self.rareMod


class Bat(Weapon):
    def __init__(self):
        super(Bat, self).__init__(Weapon.WEAPONTYPE[1])
        self.damage = random.randint(3, 7) * self.rareMod
        self.stamina = random.randint(5, 8) + self.rareMod
        self.agi = random.randint(5, 8) + self.rareMod
        self.iq = random.randint(0, 4) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod


class Mace(Weapon):
    def __init__(self):
        super(Mace, self).__init__(Weapon.WEAPONTYPE[2])
        self.damage = random.randint(2, 6) * self.rareMod
        self.stamina = random.randint(5, 10) + self.rareMod
        self.agi = random.randint(5, 10) + self.rareMod
        self.iq = random.randint(0, 8) + self.rareMod
        self.luck = random.randint(0, 8) + self.rareMod


class Stick(Weapon):
    def __init__(self):
        super(Stick, self).__init__(Weapon.WEAPONTYPE[3])
        self.damage = random.randint(7, 10) * self.rareMod
        self.stamina = random.randint(7, 10) + self.rareMod
        self.agi = random.randint(7, 10) + self.rareMod
        self.iq = random.randint(5, 10) + self.rareMod
        self.luck = random.randint(5, 10) + self.rareMod


class Gun(Weapon):
    def __init__(self):
        super(Gun, self).__init__(Weapon.WEAPONTYPE[4])
        self.damage = random.randint(7, 10) * self.rareMod
        self.stamina = random.randint(4, 8) + self.rareMod
        self.agi = random.randint(4, 8) + self.rareMod
        self.iq = random.randint(4, 7) + self.rareMod
        self.luck = random.randint(4, 7) + self.rareMod


class Bow(Weapon):
    def __init__(self):
        super(Bow, self).__init__(Weapon.WEAPONTYPE[5])
        self.damage = random.randint(7, 10) * self.rareMod
        self.stamina = random.randint(2, 6) + self.rareMod
        self.agi = random.randint(2, 6) + self.rareMod
        self.iq = random.randint(5, 9) + self.rareMod
        self.luck = random.randint(5, 9) + self.rareMod


class Staf(Weapon):
    def __init__(self):
        super(Staf, self).__init__(Weapon.WEAPONTYPE[6])
        self.damage = random.randint(5, 10) * self.rareMod
        self.stamina = random.randint(3, 6) + self.rareMod
        self.agi = random.randint(3, 6) + self.rareMod
        self.iq = random.randint(5, 8) + self.rareMod
        self.luck = random.randint(5, 8) + self.rareMod

class Boomerang(Weapon):
    def __init__(self):
        super(Boomerang, self).__init__(Weapon.WEAPONTYPE[7])
        self.damage = random.randint(5, 10) * self.rareMod
        self.stamina = random.randint(3, 6) + self.rareMod
        self.agi = random.randint(3, 6) + self.rareMod
        self.iq = random.randint(7, 10) + self.rareMod
        self.luck = random.randint(7, 10) + self.rareMod