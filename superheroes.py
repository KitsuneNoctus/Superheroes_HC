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

    def attack(self):
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()

        return total_attack

        pass
#---------------------------------------------
    def add_armor(self, armor):
        self.armors.append(armor)
        pass
#-------Defend, To be called in take Damage---------
    def defend(self, incoming_damage):
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.block()
        return total_defense

        pass
#--------------------------------------------
    def take_damage(self, damage):
        damage_taken = damage - self.defend(damage)
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
        '''Update kills with num_kills'''
        self.kills += num_kills
        pass

    def add_deaths(self, num_deaths):
        '''update deaths with num_deaths'''
        self.deaths += num_deaths
        pass

    def fight(self,opponent):
        """opponent will be a hero class"""
        both_alive = True
        print("Hero 1: "+self.name)
        print("Hero 2: " +opponent.name)
        while both_alive:
            if len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print("Draw!")
            else:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
                # print(self.current_health)
                # print(opponent.current_health)
                if opponent.is_alive() == False:
                    both_alive = False
                    print(self.name + " won!")
                    kills += 1
                elif self.is_alive() == False:
                    both_alive = False
                    print(opponent.name + "won!")
                    deaths += 1
        add_kill(kills)
        add_deaths(deaths)
        pass




#===================Team Class=====================
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

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
        # if len(self.heroes) == 0:
        #     return 0
        # else:
        #     # index_num = self.heroes.index(self.name)
        #     # self.heroes.pop(index_num)\
        #     if name in self.heroes
        #     for hero in self.heroes:
        #         if hero.name == name:
        #             self.heroes.remove(hero)

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        hero = self.heroes[random.randint(0,len(self.heroes)-1)]
        other_hero = other_team.heroes[random.randint(0,len(other_team.heroes)-1)]
        hero.fight(other_hero)
        # Hint: Use the fight method in the Hero class.

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health += health
        pass

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        for hero in self.heroes:
            print(f"Hero: {hero.name} | Deaths: {hero.deaths} | Kills: {hero.kills}")
        # Hint: Use the information stored in each hero.
        pass


if __name__=="__main__":
    #If you run this file from terminal
    #this block is executed

    hero1 = Hero("Wonder Woman",100)
    hero2 = Hero("Dumbledore",100)
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.current_health)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.current_health)
    # print(hero.is_alive())

    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)

    # ability = Ability("Roasting Ability",100)
    # ability2 = Ability("DEATH",10)
    #
    # armor = Armor("Mighty Armor",2000)
    # armor2 = Armor("Great Armor", 1000)
    #
    # hero.add_ability(ability)
    # hero.add_ability(ability2)
    #
    # hero.add_armor(armor)
    # hero.add_armor(armor2)
    #
    # print(hero.defend(10000))
    # print(hero.attack())
