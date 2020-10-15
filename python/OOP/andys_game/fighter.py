import random

class fighter:
    def __init__(self,role,name="name"):
        self.name=name
        luck = round(random.random()*10)
        if role == '1':
            self.role = Warrior(luck)
        elif role == '2':
            self.role = Mage(luck)
        elif role == '3':
            self.role = Ninja(luck)
            
    def isLucky(self):
        #luck stat * 2 % > random number(0-1) then you are lucky
        if random.random() > self.role.luck*0.02 :
            return False
        else:
            return True
                
    def attack(self, new_fighter):
        #attack value = random(0-5) + self attack stat - opponent defense stat
        amount = round(random.random()*5) + self.role.attack - new_fighter.role.defense
        #if lucky double damage
        if self.isLucky():
            amount*=2
            print('*'+self.name,"gets a critical hit*")
        #decrease opponent's health
        new_fighter.role.health -= amount
        print(self.name,"hits",new_fighter.name,"for",amount,"damage")
        
        
    def defend(self):
        #if lucky dodge attack
        if self.isLucky():
            print('*'+self.name,"dodged the attack*")
            return True
        else:
            print(self.name,"was not able to dodge the attack")
            return False
        
    def eatBerry(self):
        heal=5
        if self.isLucky():
            heal*=2
            print('*'+self.name,"ate a golden berry*")
        #increase health and check if exceeded max health
        self.role.health += heal
        if self.role.health > self.role.maxhealth:
            self.role.health = self.role.maxhealth
            
        print('Yummy!', self.name,"heals for",heal,"damage")
    
    def reset(self):
        self.role.health = self.role.maxhealth


class Warrior:
    def __init__(self,luck_stat):
        self.health = 60
        self.maxhealth = 60
        self.attack = 8
        self.defense = 7
        self.luck = luck_stat
        self.type = 'Warrior'
        

class Mage:
    def __init__(self,luck_stat):
        self.health = 45
        self.maxhealth = 45
        self.attack = 12
        self.defense = 3
        self.luck = luck_stat+2
        self.type = 'Mage'
        
class Ninja:
    def __init__(self,luck_stat):
        self.health = 50
        self.maxhealth = 50
        self.attack = 10
        self.defense = 5
        self.luck = luck_stat
        self.type = 'Ninja'