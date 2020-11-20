import random

# Armor Class


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randrange(self.max_block // 2, self.max_block)
