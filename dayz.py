# Script Name   : dayz.py
# Author        : Dylan Morrissey
# Created       : 2nd April 2019
# Description   : This is a short cmd text based game which makes use of classes and inheritance in python.
import random

class OpeningScene(object):
    print "You have been on a hike in the hills by your self for the past week."
    print "You notice that you are running low on food and water and decide to head to the nearest town."
    print "On the way to the town you notice notice the streets are very quite."
    print "You hear someone screaming run while being chased by something human like."
    print "Unfortuntley the person falls and it is a horrific sight as the person is being eaten alive."
    print "You stand in shock then suddenly the fallen man stand up and starts charging at you."
    print "You run as fast as you can and lose what ever that thing was."
    print "Worried of what you have seen you try to get help and go to the nearest shop and see it is completely empty."
    print "You hear an emergency broadcast playing on the radio warning of a zombie infection."
    print "The broadcast warn's all to stay away from the zombie's and try to make it to a safe haven in new dawn..."
    raw_input("Press enter:")
    print "\n\n"
    
class Scene(object):

    def scene(self):
        print "This scence is not yet configured"

class GameOver(Scene):
    
    def scene(self):
        print "Luck was not on you're side today so you made a bad choice and died."
        print "GAME OVER!!!"
        exit()

class Completed(Scene):

    def scene(self):
        print "You found Survival."
        print "You are safe for now but how long will this safty last."
        print "CONGRATULATIONS YOU HAVE COMPLETED THE GAME."
        exit()

class Town(Scene):

    def scene(self):
        try:
            self.option = int(raw_input("Chose your next move.\n1) Go to the police station.\n2) Go to the grocery store.\n3) Go to the nearest Gun Store.\nPlease select an option: "))
            self.playerChoice()
        except ValueError:
            print "\nNot a valid option.\n"
            self.scene()

    def playerChoice(self):
        if self.option == 1:
            print "You decide to go the the police station in search of some armor and wepons..."
            PoliceStation().scene()
        elif self.option == 2:
            print "You head towards the grocery store..."
            GroceryShop().scene()
        elif self.option == 3:
            print "You go in search of a gun store..."
            GameOver().scene()
        else:
            print "\nNot a valid option.\n"
            self.scene()
        
class PoliceStation(Scene):

    def __init__(self):
        self.policescenes = ["Survivors", "Zombies", "Gear"]
        self.randscene = random.choice(self.policescenes)

    def scene(self):
        if self.randscene == "Survivors":
            # Scene for Survivors
            print "Upon arriving at the police staDytion:"
            print "You notice a group of survivors."
            print "The question you at gun point."
            print "Survivor1: Who are you?"
            raw_input("Your Reply: ")
            print "You tell the survivors where you have been and where you are going, they agree to bring you with them as they too are heading to new dawn.\n"
            Completed().scene()
            
        elif self.randscene == "Zombies":
            # Scene for Zombies
            print "You enter the police station and try to locate the armory in the pitch black."
            print "You hear something move and start to panic."
            print "You so desperitly search for an exit."
            print "You get trapped in a dead end as the sound are coming closer."
            print "Its a whored of zombies."
            GameOver().scene()
        else:
            # Scene for Gear
            print "You make it to the police station and find some riot gear and an M4A1 with 30 Rounds in the Mag, Not much but better then nothing."
            print "You also found the keys to one of the cruiser's outside."
            Completed().scene()
        
class GroceryShop(Scene):
    
    def __init__(self):
        self.groceryscenes = ["Food", "Empty", "Military"]
        self.randscene = random.choice(self.groceryscenes)

    def scene(self):
        if self.randscene == "Food":
            print "You found a grocery store and it lookes stocked."
            print "You take what you think will be most valuable and the longest shelf life."
            print "You decide that you have enough food and find a nice shelter to keep safe while you signal for help."
            print "You call for help on every radio frequency you can."
            self.faith = random.randint(1,2)
            if self.faith == 1:
                print "Lucky you hear a faint sound on the radio."
                print "It is the UN army looking for any survivors."
                print "You tell them your coordinates and they advise they will send a helicopter to pick you up."
                Completed().scene()
            else:
                print "Unfortuntly you never brought a can opener to open the food."
                print "You try open a can with your knife but cut yourself and scream."
                print "You look out the window and see zombies surrounding your building"
                print "You have no escape and starve to death."
                GameOver().scene()
        elif self.randscene == "Empty": 
            print "You enter the grocery shop to find it is completly empty you only  find out of date food."
            print "You walk outside only to be held at gun point by a group of survivors."
            print "They loot all your belonging and tie you up and leave you for the zombies."
            GameOver().scene()
        else:
            print "Just outside the grocery shop you see what looks an abandonded military checkpoint."
            print "You look inside the Hummve and see the keys in the ignition and also a map marking where new dawn is."
            print "You decide this is good enough and make way to new dawn..."
            print "You make it to the gate of new dawn and honk the horn."
            print "Armed Snipers are scoped in on you and you are asked your purpose."
            raw_input("Armed Guard 1: What is your purpose here?")
            print "The armed guard lets you in."
            Completed().scene()

OpeningScene()
Town().scene()
