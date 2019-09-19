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

if __name__=="__main__":
    #If you run this file from terminal
    #this block is executed
    ability = Ability("Roasting Ability",100)
    armor = Armor("Midget Armor",2000)
    print(ability.name)
    print(ability.attack())
    print(armor.name)
    print(armor.block())

# class Hero:
#     def __init__(self, name, starting_health):
#         self.starting_health = 100
#         pass
#
#     def attack(self):
#         pass
#     def defend(self, incoming_damage):
#         pass
#
#     def take_damage(self, damage):
#         pass
#
#     def is_alive(self):
#         pass
#
#     def fight(self,opponent):
#         """opponent will be a hero class"""
#         pass
