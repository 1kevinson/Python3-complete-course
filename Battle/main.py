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
    print(bcolors.HEADER, bcolors.BOLD, 'WELCOME TO THE RPG GAME!', bcolors.END)
    print('===================================')
    player.choose_action()
    choice = input('\n' + 'Choose action: ')
    indexChosen = int(choice) - 1

    if indexChosen == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print('You attacked for', dmg, 'points of damage.')
    elif indexChosen == 1:
        player.choose_magic()
        magic_choice = int(input('\n' + 'Choose magic: ')) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)
        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + '\nNot enough MP\n' + bcolors.END)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OK_BLUE + '\n' + spell, 'deals', str(magic_dmg), 'points of damage' + bcolors.END)

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print('Ennemy attacked for', enemy_damage)

    print('----------------------------------------')
    print('Enemy HP:', bcolors.FAIL + str(enemy.get_hp()) + '/' + str(enemy.get_max_hp()) + bcolors.END + '\n')
    print('Your HP:', bcolors.OK_GREEN + str(player.get_hp()) + '/' + str(player.get_max_hp()) + bcolors.END)
    print('Your MP:', bcolors.OK_GREEN + str(player.get_mp()) + '/' + str(player.get_max_mp()) + bcolors.END + '\n')

    if enemy.get_hp() == 0:
        print(bcolors.OK_GREEN + 'You win!' + bcolors.END)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + 'You Lose' + bcolors.END)
        running = False
