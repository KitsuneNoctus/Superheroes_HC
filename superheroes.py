#superheroes.py
import random
class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        '''Create Instance Variables:
          name:String
          max_damage: Integer
        '''
        # TODO: Instantiate the variables listed in the docstring with then
        # values passed in
        pass

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0,self.max_damage)

        pass



class Armor:
    def __init__(self, name, max_block):
        """ name takes in string, max_block is an int"""
        self.name = name
        self.max_block = max_block
        pass

    def block(self):
        return random.randint(0,self.max_block)
        pass

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.abilities = []
        self.armors = []
        self.current_health = starting_health

        pass

    def add_ability(self, ability):
        """ Add ability to abilities list """
        self.abilities.append(ability)
        pass

    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()

        return total
        
        pass

    def defend(self, incoming_damage):
        pass

    def take_damage(self, damage):
        pass

    def is_alive(self):
        pass

    def fight(self,opponent):
        """opponent will be a hero class"""
        pass


if __name__=="__main__":
    #If you run this file from terminal
    #this block is executed

    ability = Ability("Roasting Ability",100)
    ability2 = Ability("DEATH",10)
    # armor = Armor("Midget Armor",2000)
    # print(ability.name)
    # print(ability.attack())
    # print(armor.name)
    # print(armor.block())
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(ability2)
    # print(my_hero.name)
    # print(my_hero.current_health)
    #print(hero.abilities)
    print(hero.attack())
