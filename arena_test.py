from random import randint, choice
import superheroes


# Helper Functions

def int_input(txt, default=0):
    try:
        val = int(input(txt))
    except Exception:
        return default
    return val

class Arena:

    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("What do you want the name of the ability to be?  ")
        max_damage = int_input(
            "What is the max damage you want the ability to have?  ")  # Defaults to 0
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What do you want the name of the weapon to be?  ")
        max_damage = int_input(
            "What is the max damage that you want the weapon to have?  ")
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What do you want the name of the armor to be?  ")
        max_block = int_input("How much damage do you want it to absorb?  ")
        return Armor(name, max_block)

    def create_hero(self):
        name = input("Welcome to the hero creator! What do you want the name of your hero to be?  ")
        health = int_input("Great name! Now you can change the health of your character! (default: 100)  ", 100)
        hero = Hero(name, health)
        add_abilities = input("Awesome! Would you like to add some abilities? (y/n)  ")
        if 'y' in add_abilities.lower():
            #TODO: Refactor
            while True:
                ability = self.create_ability()
                hero.add_ability(ability)
                another_ability = input("Would you like to add another ability? (y/n)  ")
                if "y" not in another_ability.lower():
                    break


        add_weapons = input("Nice abilities!  Would you like to add some weapons to your hero? (y/n)  ")
        if 'y' in add_weapons.lower():
            while True:
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
                another_weapon = input("Would you like to add another weapon? (y/n)  ")
                if "y" not in another_weapon.lower():
                    break

        add_armor = input("Those weapons seem deadly.  Finally, would you like to add some armor? (y/n)  ")
        if 'y' in add_armor.lower():
            while True:
                armor = self.create_armor()
                hero.add_armor(armor)
                another_armor = input("Would you like to add some more armor? (y/n)  ")
                if "y" not in another_armor.lower():
                    break
        return hero

    def build_team_one(self):
        name_of_team = input("Welcome to the team one builder! What do you want the name of your team to be?  ")
        num_of_heros = int_input("How many heros would you like to add to team one?  ")
        self.team_one = Team(name_of_team)

        for _ in range(num_of_heros):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):

        name_of_team = input("Welcome to the team two builder! What do you want the name of your team to be?  ")

        num_of_heros = int_input("How many heros would you like to add to team two?  ")

        self.team_two = Team(name_of_team)
        for _ in range(num_of_heros):

            hero = self.create_hero()

            self.team_two.add_hero(hero)

    def build_teams(self):

        self.build_team_one()

        self.build_team_two()

    def revive_teams(self):

        self.team_one.revive_heroes()

        self.team_two.revive_heroes()

    def team_battle(self):

        self.team_one.attack(self.team_two)

    def show_stats(self):
        t1_stats = self.team_one.stats()
        t2_stats = self.team_two.stats()
        if t1_stats > t2_stats:
            print(f"{self.team_one.name} wins the game!")
        elif t1_stats < t2_stats:
            print(f"{self.team_two.name} wins the game!")
        else:
            print("Draw")

class Ability:

    def __init__(self, name, attack_strength):

        self.name = name

        self.max_damage = attack_strength

    def attack(self):

        return randint(0, self.max_damage)

class Weapon(Ability):

    def attack(self):

        return randint(self.max_damage // 2, self.max_damage)

class Armor:

    def __init__(self, name, max_block):

        self.name = name

        self.max_block = max_block

    def block(self):

        return randint(0, self.max_block)

class Team:

    def __init__(self, name):

        self.name = name

        self.heroes = []

    def add_hero(self, hero):

        self.heroes.append(hero)

    def remove_hero(self, name):

        return [self.heroes.remove(hero) for hero in self.heroes if hero.name == name] or 0

    def view_all_heroes(self):

        [print(hero.name) for hero in self.heroes]

    def attack(self, other_team):

        while self.alive_heroes() and other_team.alive_heroes():
            # If I want to be disgusting - choice(self.alive_heroes()).fight(choice(other_team.alive_heroes()))
            local_hero = choice(self.alive_heroes())
            enemy_hero = choice(other_team.alive_heroes())
            local_hero.fight(enemy_hero)

    def alive_heroes(self):

        return [x for x in self.heroes if x.is_alive()]

    def revive_heroes(self):

        # can't oneline because of assignment :((

        for hero in self.heroes:

            hero.current_health = hero.starting_health

    def stats(self):

        return [hero.hero_stats() for hero in self.heroes]

class Hero:

    def __init__(self, name, starting_health=100):

        self.abilities = []

        self.armors = []

        self.name = name

        self.starting_health = starting_health

        self.current_health = starting_health

        self.deaths = 0

        self.kills = 0

    def add_ability(self, ability):

        self.abilities.append(ability)

    def add_weapon(self, weapon):

        self.abilities.append(weapon)

    def add_armor(self, armor):

        self.armors.append(armor)

    def add_kills(self, num_kills):

        self.kills += num_kills

    def add_deaths(self, num_deaths):

        self.deaths += num_deaths

    def attack(self):

        return sum([ability.attack() for ability in self.abilities])

    def defend(self, damage_amt=0):

        return sum([armor.block() for armor in self.armors], damage_amt)

    def take_damage(self, damage):

        self.current_health = self.current_health - self.defend(damage)

    def is_alive(self):

        return self.current_health > 0

    def hero_stats(self):

        if self.deaths > 0:
            kd = self.kills // self.deaths
            print(f"Hero: {self.name} had a KD ratio of {kd}")
            return kd
        else:
            print(f"Hero: {self.name} had a KD ratio of {self.kills}")
            return self.kills
    def fight(self, opponent):

        while True:

            if self.is_alive():

                self_dmg = self.attack()

                opponent.take_damage(self_dmg)

            else:  # Opp wins

                opponent.add_kills(1)

                self.add_deaths(1)

                break
            if opponent.is_alive():

                opp_dmg = opponent.attack()

                self.take_damage(opp_dmg)

            else:  # Self wins

                self.add_kills(1)

                opponent.add_deaths(1)

                break

if __name__ == "__main__":

    game_is_running = True
    arena = Arena()
    arena.build_teams()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if "y" not in play_again.lower():
            game_is_running = False
        else:
            arena.revive_teams()
