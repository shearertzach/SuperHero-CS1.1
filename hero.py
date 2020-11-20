import random
from ability import Ability
from armor import Armor
from weapon import Weapon

# Hero Class


class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        if self.is_alive() and opponent.is_alive():
            print("A hits B")
            opponent.take_damage(self.attack())
            if opponent.is_alive():
                print("B hits A")
                self.take_damage(opponent.attack())
                if self.is_alive() is True:
                    self.fight(opponent)
                else:
                    return print(
                        f"{opponent.name} wins! {self.name} has been defeated."
                    )
            else:
                return print(
                    f"{self.name} wins! {opponent.name} has been defeated.")

    def add_ability(self, ability):
        self.abilities.append(ability)
        print(
            f"{ability.name} has been added to {self.name}'s ability arsenal.")

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        print(
            f"{weapon.name} has been added to {self.name}'s ability arsenal.")

    def add_armor(self, armor):
        self.armors.append(armor)
        print(f"{armor.name} has been added to {self.name}'s armor set.'")

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, attack_damage):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return attack_damage - total_block

    def take_damage(self, damage):
        self.current_health -= self.defend(damage)
        print(
            f"{self.name} took {damage} damage. Current Health: {self.current_health}"
        )

    def is_alive(self):
        if self.current_health < 1:
            return False
        elif self.current_health > 0:
            return True


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
