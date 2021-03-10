from random import randrange

def modifier(roll):
    return (roll - 10)//2

class Character:
    def __init__(self):
        for abilities in  ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
            self.__setattr__(abilities,self.ability)


    @property
    def ability(self):
        return sum(sorted([randrange(1,7) for i in range(5)])[1:])