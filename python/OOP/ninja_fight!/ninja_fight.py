# Exciting Game by Aki, Ashley, Greg, Lucie 

class Ninja:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None 
        self.food = None
        self.skill = None

    def displayStats(self):
        print(self.name+"'s Stats:")
        print("Health:", self.health)
        if self.weapon is not None:
            print("Weapon Damage:",self.weapon.damage)
        return self

    def displayInventory(self):
        print(f"\n{self.name}'s Inventory:")
        if self.weapon is not None:
            print("\nWeapon:", self.weapon.type)
        else:
            print("\nYou have no weapon")
        if self.food is not None:
            print("Food:", self.food.type)
        else:
            print("You have no food")    
        if self.skill is not None:
            print("Skill:", self.skill.type)
        else:
            print("You have no skill")
        return self

    def pickUpWeapon(self):
        print("\nYou see a katana, a shuriken, and an axe.")
        tempName = input("\nChoose Your Weapon: ")
        while tempName != "katana" and tempName != "shuriken" and tempName != "axe":
            print(f"\n{tempName} is not available")
            tempName = input("\nChoose Your Weapon: ")            
        if self.weapon is not None:
            print(f"\n{self.name} drops a {self.weapon.type}")
        self.weapon = Weapon(tempName)
        print(self.weapon)   
        print(f"\n{self.name} picks up a {self.weapon.type}")
        return self

    def pickUpSkill(self,skillType):
        if self.skill is not None:
           print(f"{self.name} forgets {self.skill.type}")
        self.skill = Skill(skillType)
        print(f"{self.name} learns {self.skill.type}")
        return self    

    def fight(self,otherNinja):
        print("You started a fight with",otherNinja.name)
        if self.weapon is not None:
            if self.skill is not None:
                if self.skill.type == "power up":
                    otherNinja.health -= (self.weapon.damage + 20) 
                    print("You used your", self.weapon.type,"and",self.skill.type+".",otherNinja.name,"loses",(self.weapon.damage + 20),"health points.")
                else:
                    otherNinja.health -= self.weapon.damage 
                    print("You used your", self.weapon.type+".",otherNinja.name,"loses",self.weapon.damage,"health points.")
                if otherNinja.skill is not None:
                    if otherNinja.health <=0 and otherNinja.skill.type !="cheat death":
                        print(otherNinja.name,"is DEAD!")
                    elif otherNinja.health <=0:
                        otherNinja.health = 1
                        otherNinja.skill = None
                        print(otherNinja.name,"used cheat death skill, and revived with 1 health point.")
                elif otherNinja.health <=0:
                    print(otherNinja.name,"is DEAD!")
            else:
                otherNinja.health -= self.weapon.damage 
                print("You used your", self.weapon.type+".",otherNinja.name,"loses",self.weapon.damage,"health points.")
                if otherNinja.skill is not None:
                    if otherNinja.health <=0 and otherNinja.skill.type !="cheat death":
                        print(otherNinja.name,"is DEAD!")
                    elif otherNinja.health <=0:
                        otherNinja.health = 1
                        otherNinja.skill = None
                        print(otherNinja.name,"used cheat death skill, and revived with 1 health point.")
                elif otherNinja.health <=0:
                    print(otherNinja.name,"is DEAD!")
        elif otherNinja.weapon is not None:
            if self.skill is not None:
                if self.skill.type == "cheat death":
                    self.health = 1
                    self.skill = None
                    print("You used cheat death skill, and revived with 1 health point.")
                else:
                    self.health = 0
                    print("You are DEAD!")
            else:
                self.health = 0
                print("You are DEAD!")
        else:
            self.health -= 20
            otherNinja.health -=20
            print("You got into a fist fight, both of you received -20 damage. You deserved this...")
            if self.health <= 0 and self.skill is not None:
                if self.skill.type == "cheat death":
                    self.health = 1
                    self.skill = None
                    print("You used cheat death skill, and revived with 1 health point.")
                else:
                    self.health = 0
                    print("You are DEAD!")
            elif self.health <= 0:
                self.health = 0
                print("You are DEAD!")

            if otherNinja.health <= 0 and otherNinja.skill is not None:
                if otherNinja.skill.type == "cheat death":
                    otherNinja.health = 1
                    otherNinja.skill = None
                    print(otherNinja.name,"used cheat death skill, and revived with 1 health point.")
                else:
                    otherNinja.health = 0
                    print(otherNinja.name,"is DEAD!")
            elif otherNinja.health <= 0:
                otherNinja.health = 0
                print(otherNinja.name,"is DEAD!")
        return self

    def pickUpFood(self,foodType):
        if self.food is not None:
           print(f"{self.name} drops a {self.food.type}")
        self.food = Food(foodType)
        print(f"{self.name} picks up a {self.food.type}")
        return self

    def eatFood(self):
        if self.food is not None:
            print("You ate your",self.food.type)
            self.health += self.food.heal_damage
            if self.food.heal_damage > 0:
                print("You recovered",self.food.heal_damage,"health points!")
            else:
                print("HAHAHAHAHA,tricked you, the apple is poisonous! You lose",self.food.heal_damage,"health points!!!")
                if self.health <= 0 and self.skill is not None:
                    if self.skill.type == "cheat death":
                        self.health = 1
                        print("You used cheat death skill, and revived with 1 health point.")
                    else:
                        self.health = 0
                        print("You are DEAD!")
                elif self.health <= 0:
                    self.health = 0
                    print("You are DEAD!")
            self.food = None
        else:
            print("You do not have any food!")
        return self



class Weapon:
    def __init__(self, weaponType):
        damage = {"katana":25,"shuriken":15,"axe":30}
        self.type = weaponType
        self.damage = damage[weaponType] #tested: pass!
    
class Food:
    def __init__(self, foodType):
        heal_damage = {"strawberry":10,"pizza":20,"takoyaki":8,"shiny apple":-50}
        self.type = foodType
        self.heal_damage = heal_damage[foodType]      

class Skill:
    def __init__(self, skillType):
        self.type = skillType

# def createFighter():
#     tempName = input("Enter Ninja's Name: ")
#     print(tempName)
#     characters.append(tempName)
def pickupWeapon2():
    # print(player1)
    tempName = input("Choose Your Weapon: ")
    if player1.weapon is not None:
        print(f"{player1.name} drops a {player1.weapon.type}")
    player1.weapon = Weapon(tempName)
    print(f"{player1.name} picks up a {player1.weapon.type}")
    return player1
    

#skills: "power up", "cheat death"
#weapon:Katana, Shuriken, Axe
#food: strawberry, pizza, takoyaki, **SHINY APPLE** :D 

# kikomo = Ninja("Kikomo")
# kikomo.pickUpSkill("cheat death")
characters = []

print("\nWelcome to -- NINJA FIGHT!")
tempName = input("\nName Your Ninja: ")
print(f"\nWelcome {tempName}!")
characters.append(tempName)
player1 = Ninja(characters[0])

menu=''
while menu != '4':
    print('\nWhat do you want to do?')
    menu=input("1. Show Inventory\n2. Pickup Weapon\n3. FIGHT!\n4. Exit\n\n**")
    # if menu=='1':
    #     createFighter()
    #     if len(characters)>0:
    if menu=='1':
        player1.displayInventory()        
    if menu=='2':
        player1.pickUpWeapon()

print("\nThanks for playing!")

#actions: 
# pick up a weapon
# pick up food
# learn a skill
# eat food
# fight

#anytime:
# show stats
# show inventory






