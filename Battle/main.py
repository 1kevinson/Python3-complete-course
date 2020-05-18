from Battle.classes.game import Person, bcolors

'''
HP
Health Points. 

MP
Magic Points.

DF
Defense Points.

Atkl
Attack power (low)

Atkh
Attack power (high)
'''

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 60},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

while running:
    print(bcolors.HEADER, bcolors.BOLD, 'WELCOME !', bcolors.END)
    print('===================================')
    player.choose_action()
    choice = input('Choose action: ')
    indexChoosen = int(choice) - 1

    if indexChoosen == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print('You attacked for', dmg, 'point of damage. Enemy HP:', enemy.get_hp())

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print('Ennemy attacked for', enemy_damage, 'point of damage. Player HP:', player.get_hp())