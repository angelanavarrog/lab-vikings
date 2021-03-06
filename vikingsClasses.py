


import random as rd

# Soldier

class Soldier:
    pass
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength

    def attack (self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage


# Viking

class Viking (Soldier):
    pass

    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.name + " has received " +  str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon (Soldier):
    pass

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received " +  str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"

# War

class War:
    pass