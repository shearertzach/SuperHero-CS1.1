import random

# Ability Class


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randrange(self.max_damage // 2, self.max_damage)
