import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[95m'
    OKGREEN = '\033[95m'
    WARNING = '\033[95m'
    FAIL = '\033[95m'
    ENDC = '\033[95m'
    BOLD = '\033[95m'
    UNDERLINE = '\033[95m'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['attack', 'magic']

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

    def generate_spell_damage(self, i):
        mgl = self.magic[i]['dmg'] - 5
        mgh = self.magic[i]['dmg'] + 5
        return random.randrange(mgl, mgh)

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

        return self.hp

    def choose_action(self):
        i = 1
        print('Actions :')
        for item in self.actions:
            print(str(i), ':', item)
            i += 1

    def choose_magic(self):
        i = 1
        print('Magic :')
        for item in self.magic:
            print(str(i), ':', item['name'], " (cost: ", item['cost'], ')')
            i += 1
