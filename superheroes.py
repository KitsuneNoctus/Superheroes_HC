#superheroes.py
import random
#=================Ability Class========================
class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        pass

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0,self.max_damage)
        pass

#======================Armor Class========================
class Armor:
    def __init__(self, name, max_block):
        """ name takes in string, max_block is an int"""
        self.name = name
        self.max_block = max_block
        pass

    def block(self):
        return random.randint(0,self.max_block)
        pass
#====================Weapon Class=======================
class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return random.randint(self.max_damage//2,self.max_damage)
        # TODO: Use what you learned to complete this method.
        pass
#=====================Hero Class========================
#HERO CLASS that accesses the other objects
class Hero:
    """ Builds the hero and allows them to fight"""
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.abilities = []
        self.armors = []
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

        pass
#--------------------------------------------
    def add_ability(self, ability):
        """ Add ability to abilities list """
        self.abilities.append(ability)
        pass

#-----+------Ch 5 add weapon ----------+------
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)
        pass
#------+---------------------------------+----

    def attack(self):
        """To attack the opponent"""
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()

        return total_attack

        pass

#---------------------------------------------
    def add_armor(self, armor):
        '''Add Armor to self.armor
            armor: Armor object'''
        self.armors.append(armor)
        pass
#-------Defend, To be called in take Damage---------
    def defend(self):
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.block()
        return total_defense

        pass
#--------------------------------------------
    def take_damage(self, damage):
        damage_taken = damage - self.defend()
        self.current_health = self.current_health - damage_taken
        return self.current_health
        pass

    def is_alive(self):
        """Checks to see if hero is alive"""
        if self.current_health <= 0:
            return False
        else:
            return True

        pass

    def add_kill(self, num_kills):
        '''Update kills with num_kills the hero has'''
        self.kills += num_kills
        pass

    def add_deaths(self, num_deaths):
        '''update deaths with num_deaths'''
        self.deaths += num_deaths
        pass

    def fight(self,opponent):
        """opponent will be a hero class"""
        kill_count = 0
        death_count = 0
        both_alive = True
        print("Hero 1: "+self.name)
        print("Hero 2: " +opponent.name)
        while both_alive:
            if len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print("Draw!")
                #While not true, this will kill the program
                both_alive = False
            else:
                self.take_damage(opponent.attack())

                if self.is_alive() == False:
                    self.add_deaths(1)
                    opponent.add_kill(1)
                    both_alive = False
                    print(opponent.name + " won!")
                    break

                opponent.take_damage(self.attack())

                if opponent.is_alive() == False:
                    opponent.add_deaths(1)
                    self.add_kill(1)
                    both_alive = False
                    print(self.name + " won!")
                    break



#===================Team Class=====================
class Team:
    """Allows for the creation of the team with all of its heros and their powers"""
    def __init__(self, name):
        self.name = name
        self.heroes = []
        # self.dead_heroes[]

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        if len(self.heroes) == 0:
            return 0
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return
        return 0


    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def get_dead(self, team):
        death_count = 0
        for hero in team:
            if hero.current_health == 0:
                death_count += 1

        if death_count == len(team):
            return False
        else:
            return True

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        if len(self.heroes) == 0 or len(other_team.heroes) == 0:
            print("No Contest! One or both teams has no heroes to fight!")
        else:
            #Add in loop so whole team fights
            index_get = random.randint(0,len(self.heroes)-1)
            hero = self.heroes[index_get]
            index_get_2 = random.randint(0,len(other_team.heroes)-1)
            other_hero = other_team.heroes[index_get_2]

            hero.fight(other_hero)

        # Hint: Use the fight method in the Hero class.

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health = health
        pass

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        for hero in self.heroes:
            print(f"  - Hero: {hero.name} | Deaths: {hero.deaths} | Kills: {hero.kills}")
        # Hint: Use the information stored in each hero.
        pass

#======================Arena Class======================
class Arena:
    def __init__(self):
        '''Instantiate properties
        team_one: None
        team_two: None
        '''
        self.team_one = None
        self.team_two = None
        pass

    def create_ability(self):
        ability_name = input("What is the ability name?: ")
        num_true = True
        while num_true:
            try:
                ability_max_damage = int(input(f"What is the max damage {ability_name} does?: "))
                new_ability = Ability(ability_name, ability_max_damage)
                num_true = False
            except ValueError:
                print("Not Valid, Enter proper number.")

        return new_ability

    def create_weapon(self):
        weapon_name = input("What is the weapon name?: ")
        num_true = True
        while num_true:
            try:
                weapon_max_damage = int(input(f"What is the max damage of {weapon_name}?: "))
                new_weapon = Weapon(weapon_name, weapon_max_damage)
                num_true = False
            except ValueError:
                print("Not Valid, Enter proper number.")

        return new_weapon

    def create_armor(self):
        armor_name = input("What is the armor name?: ")
        num_true = True
        while num_true:
            try:
                armor_max_block = int(input(f"What is the max defense of {armor_name}?: "))
                new_armor = Armor(armor_name, armor_max_block)
                num_true = False
            except ValueError:
                print("Not Valid, Enter proper number.")
        return new_armor
#----------Createing the heroes here ----------------
    def create_hero(self):
        #Create the hero
        hero_name = input("What is the Hero's name?: ")
        hero_change_health = input("Would you like to change hero health from 100?[Y/N]: ")
        if hero_change_health == "Y" or hero_change_health == "yes" or hero_change_health == "Yes":
            no_num = True
            while no_num:
                try:
                    hero_health = int(input("What is the heroe's new health?: "))
                    no_num = False
                except ValueError:
                    print("Not Valid Entry")
        else:
            hero_health = 100
        new_hero = Hero(hero_name, hero_health)
        print("+++")
        #--------To create heroes setup -----------
        ask_ability = input("Would you like to give them an ability?[Y/N]: ")
        if ask_ability == "Y" or ask_ability == "yes" or ask_ability == "Yes" or ask_ability == "y":
            new_hero.abilities.append(self.create_ability())
        else:
            print("No abilities added")
        print("+++")

        ask_weapon = input("Would you like to give them a weapon?[Y/N]: ")
        if ask_weapon == "Y" or ask_weapon == "yes" or ask_weapon == "Yes" or ask_weapon == "y":
            new_hero.abilities.append(self.create_weapon())
        else:
            print("No weapons added")
        print("+++")

        ask_armor = input("Would you like to give them armor?[Y/N]: ")
        if ask_armor == "Y" or ask_armor == "yes" or ask_armor == "Yes" or ask_armor == "y":
            new_hero.armors.append(self.create_armor())
        else:
            print("No armor added")
        print("+++")

        return new_hero
    #---------Creating team setup-------------
    def build_team_one(self):
        team_name = input("1st team name: ")
        self.team_one = Team(team_name)
        valid = True
        while valid:
            try:
                num_heroes = int(input(f"How many heroes do you want on team {team_name}?: "))
                valid = False
            except ValueError:
                print("Not Valid Entry, Try Again.")


        count = 0
        while count != num_heroes:
            self.team_one.heroes.append(self.create_hero())
            count += 1

        return self.team_one

    def build_team_two(self):
        team_name = input("2nd team name: ")
        self.team_two = Team(team_name)
        valid = True
        while valid:
            try:
                num_heroes = int(input(f"How many heroes do you want on team {team_name}?: "))
                valid = False
            except ValueError:
                print("Not Valid Entry, Try Again.")

        count = 0
        while count != num_heroes:
            self.team_two.heroes.append(self.create_hero())
            count += 1

        return self.team_two

    #-----------Causes battle to happen--------------
    def team_battle(self):
        """Calls the function within team class to start fight"""
        self.team_one.attack(self.team_two)

    def is_team_dead(self, team_checking):
        """Counts number of dead on the team and checks if all are dead"""
        death_count = 0
        for hero in team_checking:
            if hero.current_health <= 0:
                death_count += 1

        if death_count == len(team_checking):
            return True
        else:
            return False

    def show_stats(self):
        """Will display the winner, then it will show the stats of the heros who fought"""
        winner = ""
        team_1_alive = self.is_team_dead(self.team_one.heroes)
        team_2_alive = self.is_team_dead(self.team_two.heroes)
        if team_1_alive == False and team_2_alive == False:
            print("The match is a draw!")
        elif team_1_alive == False:
            winner = self.team_one.name
            print(f"Winner is team {winner}!")
            print(f"Heroes left alive from team {winner}")
            for hero in self.team_one.heroes:
                # print(hero.current_health)
                if hero.current_health > 0:
                    print(hero.name)
        elif team_2_alive == False:
            winner = self.team_two.name
            print(f"Winner is team {winner}!")
            print(f"Heroes left alive from {winner}")
            for hero in self.team_two.heroes:
                # print(hero.current_health)
                if hero.current_health > 0:
                    print(hero.name)
        else:
            print("-Null-")


        print(f"Team {self.team_one.name} stats:")
        self.team_one.stats()
        print(f"Team {self.team_two.name} stats:")
        self.team_two.stats()

        pass



if __name__=="__main__":
    game_on = True
    print("++++++++++++++++++++++++++++++")
    print("Welcome to Super Hero Dueler!")
    print("++++++++++++++++++++++++++++++")
    while game_on:
        """Allows for the game to keep running/ to change teams or create new ones later """
        play_inquery = input("Would you like to play?[Y/N]")
        if play_inquery.lower() == "y" or play_inquery.lower() == "yes":
            game_running = True
            arena = Arena()
            arena.build_team_one()
            arena.build_team_two()
            match_count = 1
            while game_running:
                print(f"Match {match_count}")
                arena.team_battle()
                arena.show_stats()

                play_again = input("Play these teams again?[Y/N]: ")
                if play_again.lower() == "n" or play_again.lower() == "no":
                    game_running = False
                else:
                    match_count += 1
                    arena.team_one.revive_heroes()
                    arena.team_two.revive_heroes()
        elif play_inquery.lower() == "n" or play_inquery.lower() == "no":
            print("Exiting")
            game_on = False
        else:
            print("Not Valid Entry")
