import random


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def add_hero(self, hero):
        self.heroes.append(hero)

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = 100

    def attack(self, opponent_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in opponent_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            loser = hero.fight(opponent)
            # 3) update the list of living_heroes and living_opponents
            for hero in living_heroes:
                if loser == hero.name:
                    living_heroes.remove(hero)
            for opponent in living_opponents:
                if loser == opponent.name:
                    living_opponents.remove(opponent)
            # to reflect the result of the fight
