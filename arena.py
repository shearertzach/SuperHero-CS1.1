from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self, team_one, team_two):
        self.team_one = team_one
        self.team_two = team_two

    def create_ability(self):
        name = input("What is the ability name?  ")
        max_damage = int(input(
            "What is the max damage of the ability?  "))

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name?  ")
        max_damage = int(input(
            "What is the max damage of the weapon?  "))

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the name of the armor?")
        max_block = int(input("what is the max block of the armor?"))

        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability_to_add = self.create_ability()
                hero.add_ability(ability_to_add)
            elif add_item == "2":
                weapon_to_add = self.create_weapon()
                hero.add_weapon(weapon_to_add)
            elif add_item == "3":
                armor_to_add = self.create_weapon()
                hero.add_armor(armor_to_add)
        return hero

    def build_team_one(self):
        numOfTeamMembers = int(
            input("How many members would you like on Team One?\n"))
        for _ in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        numOfTeamMembers = int(
            input("How many members would you like on Team Two?\n"))
        for _ in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def team_one_stats(self):
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " +
              str(team_kills/team_deaths))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

    def team_two_stats(self):
        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " average K/D was: " +
              str(team_kills/team_deaths))

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)

    def show_stats(self):
        print(f"SHOWING TEAM ONE STATS")
        self.team_one_stats()
        print(f"SHOWING TEAM TWO STATS")
        self.team_two_stats()


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena(Team("Avengers"), Team("DC"))

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
