init python:
    class RPGStats:
        def __init__(self, hp, atk, defence, crit, acc, evd):
            self.hp = hp
            self.atk = atk
            self.defence = defence
            self.crit = crit
            self.acc = acc
            self.evd = evd

    rpg_characters = {
        "alban": RPGStats(
            hp=100, atk=10, defence=10,
            crit=10, acc=10, evd=10,
        ),
        "fulgur": RPGStats(
            hp=100, atk=10, defence=10,
            crit=10, acc=10, evd=10,
        ),
        "protag": RPGStats(
            hp=100, atk=10, defence=10,
            crit=10, acc=10, evd=10,
        ),
        "sonny": RPGStats(
            hp=100, atk=10, defence=10,
            crit=10, acc=10, evd=10,
        ),
        "uki": RPGStats(
            hp=100, atk=10, defence=10,
            crit=10, acc=10, evd=10,
        ),
    }