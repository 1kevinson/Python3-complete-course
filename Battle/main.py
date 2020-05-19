from Battle.classes.game import Person, bcolors
from Battle.classes.magic import Spell

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

#Create Black Magic
fire = Spell('Fire',10,100,'black')
thunder = Spell('Thunder',10,100,'black')
blizzard = Spell('Blizzard',10,100,'black')
meteor = Spell('Meteor',10,200,'black')
quake = Spell('Quake',14,140,'black')

#Create white magic
cure = Spell('Cure',12,120,'white')
cura = Spell('Cure',18,200,'white')

magic_array = [fire, thunder,blizzard,meteor,cure,cura]

#Instanciate people
player = Person(460, 65, 60, 34, magic_array)
enemy = Person(1200, 65, 45, 25, magic_array)

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

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + '\nNot enough MP\n' + bcolors.END)
            continue

        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OK_BLUE + '\n' + spell.name, 'deals', str(magic_dmg), 'points of damage' + bcolors.END)

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
