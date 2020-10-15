import fighter
import time
import random

def createFighter():
    tempname=input("Enter Fighter's Name: ").capitalize()
    print("\nWelcome "+tempname+"!\n")

    tempclass=''
    while tempclass not in ('1','2','3'):
        tempclass=input("Pick a class:\n1. Warrior [HP: 60 ATK:  8 DEF: 7]\n2. Mage    [HP: 45 ATK: 12 DEF: 3]\n3. Ninja   [HP: 50 ATK: 10 DEF: 5]\n:")
        if tempclass not in ('1','2','3'):
            print("Invalid choice. Please pick again!")
    characters.append(fighter.fighter(tempclass,tempname))
    print(characters[len(characters)-1].name, "the", characters[len(characters)-1].role.type, "was created!")


def displayFighters():
    print("List of Fighters:")
    for i in range(len(characters)):
        print('\n'+str(i+1)+'.')
        print("Name: ", characters[i].name)
        print("Class:", characters[i].role.type)
        print("HP:   ", characters[i].role.attack)
        print("ATK:  ", characters[i].role.attack)
        print("DEF:  ", characters[i].role.defense)
        print("LCK:  ", characters[i].role.luck)

        
def initFight():
    #no error checking here at the moment or removing player1 from the list of opponents
    print("Pick your fighter:")
    time.sleep(2)
    displayFighters()
    player1=int(input("(Your fighter):"))
    print("Pick your opponent:")
    time.sleep(2)
    displayFighters()
    player2=int(input("(Opponent):"))
    fight(player1,player2)
          

def fight(p1,p2):
    p1-=1
    p2-=1       
    #fight loop until one characters <= 0
    while True:
        spacer=' '*(len(characters[p1].name)+3)
        print('\n'+characters[p1].name+"'s HP"+'   '+characters[p2].name+"'s HP")
        print(' ',characters[p1].role.health, spacer, characters[p2].role.health)
        
        
        if (characters[p1].role.health <= 0) and (characters[p2].role.health <= 0):
            print("You both killed each other... Villagers wander by and wonder what idiocracy occured here..\n")
            characters[p1].reset()
            characters[p2].reset()
            return
        
        if (characters[p1].role.health <= 0):
            print(characters[p1].name,"gasps as",characters[p2].name+"'s","attack depletes the last bit of remaining life.")
            print(characters[p2].name, "is victorious!\n")
            characters[p1].reset()
            characters[p2].reset()
            return
            
        if (characters[p2].role.health <= 0):
            print(characters[p1].name,"stands over",characters[p2].name+"'s","lifeless body and cackles.")
            print(characters[p1].name, "is victorious!\n")
            characters[p1].reset()
            characters[p2].reset()
            return
        
        opp_act=random.randint(1,3)
        action = ''
        while action not in ('1','2','3'):
        
            action=input('\n1.Attack\n2.Dodge\n3.Eat a Berry\n:')
            print(characters[p2].name+" picked",opp_act,'\n')
            
            #not efficient but check for each possible combination of actions
            if action == '1':
                if opp_act == 1:
                    characters[p1].attack(characters[p2])
                    characters[p2].attack(characters[p1])
                elif opp_act == 2:
                    if not characters[p2].defend():
                        characters[p1].attack(characters[p2])
                elif opp_act == 3:
                    characters[p2].eatBerry()
                    characters[p1].attack(characters[p2])
                  
            elif action == '2':
                if opp_act == 1:
                    if not characters[p1].defend():
                        characters[p2].attack(characters[p1])
                elif opp_act == 2:
                    print("Both of you stare into each other's eyes waiting to see who flinches first...")
                elif opp_act == 3:
                    characters[p2].eatBerry()
                    print(characters[p1].name, "watches "+characters[p2].name+" eat that berry and wonders why you didn't attack")
                   
            elif action == '3':
                characters[p1].eatBerry()
                if opp_act == 1:
                    characters[p2].attack(characters[p1])
                elif opp_act == 2:
                    print(characters[p2].name, "wishes he could have a bite of that berry :(\n")
                elif opp_act == 3:
                    characters[p2].eatBerry()
            else:
                print("Invalid Selection\n")
        

#start of game
characters=[]    
     
menu=''
while menu != '4':
    print('\nMAIN MENU')
    menu=input("1. Create a Fighter\n2. View Fighters\n3. FIGHT!\n4. Exit\n:")
    
    if menu=='1':
        createFighter()
    if menu=='2':
        displayFighters()
    if menu=='3':
        initFight()

print("\nThanks for playing!")