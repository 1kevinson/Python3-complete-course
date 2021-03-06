import random


class bcolors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['attack', 'magic', 'items']

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def reduce_mp(self, cost):
        self.mp -= cost

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def choose_action(self):
        i = 1
        print(bcolors.OK_BLUE + bcolors.BOLD + 'Actions :' + bcolors.END)
        for item in self.actions:
            print(str(i), ':', item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OK_BLUE + bcolors.BOLD + 'Magic :' + bcolors.END)
        for item in self.magic:
            print(str(i), ':', item.name, "(cost:", item.cost, ')')
            i += 1

    def choose_item(self):
        i = 1
        print(bcolors.OK_BLUE + bcolors.BOLD + 'Items :' + bcolors.END)
        for item in self.items:
            print(str(i), ':', item['item'].name, ":", item['item'].description, "(x", item['quantity'], ")")
            i += 1
