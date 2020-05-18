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

print(player.genearete_spell_damage(0))
print(player.genearete_spell_damage(1))

