import random


# Define a class
class Enemy:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)

    def getHP(self):
        print(self.hp)


enemy = Enemy(12, 55)
enemy.getAtk()
enemy.getHP()
'''

playerHP = 250
enemyATKL = 40
enemyATKH = 60

while playerHP > 0:
    damage = random.randrange(enemyATKL, enemyATKH)
    playerHP = playerHP - damage

    if playerHP <= 30:
        playerHP = 30

    print('Enemy strikes > ', damage, 'points of damage. Current HP is ', playerHP)

    if playerHP > 30:
        continue

    print('Teleported to the inn :(')
    break

'''

# Typo
'''
    Every method in python have a self parameter which refer to the entire object
    __init__ refer to constructor
'''
