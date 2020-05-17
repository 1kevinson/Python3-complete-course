import random

playerHP = 250
enemyATKL = 40
enemyATKH = 60

while playerHP > 0:
    damage = random.randrange(enemyATKL,enemyATKH)
    playerHP = playerHP - damage

    if playerHP <= 30:
        playerHP = 30

    print('Enemy strikes > ', damage, 'points of damage. Current HP is ', playerHP)

    if playerHP == 30:
        print('Teleported to the inn :(')
        break