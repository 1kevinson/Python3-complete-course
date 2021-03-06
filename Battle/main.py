from Battle.classes.game import Person, bcolors
from Battle.classes.magic import Spell
from Battle.classes.inventory import Item

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

# BARS
print('\n')
print('NAME                 HP                            MP')
print('                     _________________             _________________  ')
print(bcolors.BOLD + 'VALOS:      ' +
      '460/460 |' + bcolors.OK_GREEN + '█████████████████' + bcolors.END + bcolors.BOLD + '|    ' +
      ' 65/65 |' + bcolors.OK_BLUE + '█████████████████' + bcolors.END + '| ')

print('                     _________________             _________________  ')
print('VALOS:      460/460 |                 |     65/65 |                 | ')

print('                     _________________             _________________  ')
print('VALOS:      460/460 |                 |     65/65 |                 | ')

print('\n')

# Create Black Magic
fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('Thunder', 10, 100, 'black')
blizzard = Spell('Blizzard', 10, 100, 'black')
meteor = Spell('Meteor', 10, 200, 'black')
quake = Spell('Quake', 14, 140, 'black')

# Create white magic
cure = Spell('Cure', 12, 120, 'white')
cura = Spell('Cure', 18, 200, 'white')

# Create Item
potion = Item('Potion', 'potion', 'Heals 50 HP', 50)
hiPotion = Item('Hi-Potion', 'potion', 'Heals 100 HP', 100)
superPotion = Item('Super Potion', 'potion', 'Heals 500 HP', 500)
elixer = Item('Elixer', 'elixer', 'Fully restore HP/MP of a party member', 9999)
hiElixer = Item('MegaElixir', 'elixer', 'Fully restores  party\'s HP/MP', 9999)

grenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)

# Create array of magics
magic_array = [fire, thunder, blizzard, meteor, cure, cura]
item_array = [{'item': potion, 'quantity': 15}, {'item': hiPotion, 'quantity': 5}, {'item': superPotion, 'quantity': 5},
              {'item': elixer, 'quantity': 5}, {'item': hiElixer, 'quantity': 2}, {'item': grenade, 'quantity': 5}]

# Instanciate people
player = Person(460, 65, 60, 34, magic_array, item_array)
enemy = Person(1200, 65, 45, 25, [], [])

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

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + '\nNot enough MP\n' + bcolors.END)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == 'white':
            player.heal(magic_dmg)
            print(bcolors.OK_BLUE + '\n' + spell.name, 'heals for', str(magic_dmg), 'HP.' + bcolors.END)
        elif spell.type == 'black':
            enemy.take_damage(magic_dmg)
            print(bcolors.OK_BLUE + '\n' + spell.name, 'deals', str(magic_dmg), 'points of damage' + bcolors.END)
    elif indexChosen == 2:
        player.choose_item()
        item_choice = int(input('\n' + 'Choose item : ')) - 1

        if item_choice == -1:
            continue

        if player.items[item_choice]['quantity'] == 0:
            print(bcolors.FAIL + '\n' + 'None left...' + bcolors.END)

        item = player.items[item_choice]['item']
        player.items[item_choice]['quantity'] -= 1

        if item.type == 'potion':
            player.heal(item.prop)
            print(bcolors.OK_BLUE + '\n' + item.name, 'heals for', str(item.propa), 'HP.' + bcolors.END)
        elif item.type == 'elixer':
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OK_GREEN + '\n' + item.name, 'fully restores HP/MP' + bcolors.END)
        elif item.type == 'attack':
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + '\n' + item.name, 'deals', str(item.prop), 'points of damage' + bcolors.END)

    # Enemy section ( choose 1 by default to perform an attack)
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
        print(bcolors.FAIL + 'Enemy defeated you' + bcolors.END)
        running = False
