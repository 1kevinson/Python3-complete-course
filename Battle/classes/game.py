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
    def __init__(self, hp, mp, atk,df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['attack','magic']

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)