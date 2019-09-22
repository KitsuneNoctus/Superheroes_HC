#superheroes.py
import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        pass

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0,self.max_damage)
        pass

#=========================================================
class Armor:
    def __init__(self, name, max_block):
        """ name takes in string, max_block is an int"""
        self.name = name
        self.max_block = max_block
        pass

    def block(self):
        return random.randint(0,self.max_block)
        pass
#=========================================================
#HERO CLASS that accesses the other objects
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.abilities = []
        self.armors = []
        self.current_health = starting_health

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
        if self.current_health <= 0:
            return False
        else:
            return True

        pass

    def fight(self,opponent):
        """opponent will be a hero class"""
        pass


if __name__=="__main__":
    #If you run this file from terminal
    #this block is executed

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.current_health)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.current_health)
    print(hero.is_alive())

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
