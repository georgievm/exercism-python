from random import randint
ABILITIES = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

class Character:
    def __init__(self):
        for a in ABILITIES:
            setattr(self, a, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        four_dice = sorted([randint(1, 6) for _ in range(4)])
        return sum(four_dice[1:])

def modifier(constitution):
    return (constitution - 10) // 2
