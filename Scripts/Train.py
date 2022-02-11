from doctest import master
from random import Random, random
from re import L
from zxtouch.client import zxtouch 
from zxtouch.touchtypes import *
import time
import random

#DEVICE IP 
device = zxtouch("192.168.1.177")

#Button Coordinates

Blanche = (200,1075)
Candela = (375,1075)
Spark = (550,1075)

TrainButton = (375,1030)

Great = (375,600)
Ultra =  (375,800)
Master = (375,1000)

UseParty = (375, 1225)
XButton =  ("375", "1230")
StartArea = (375,50)


#Button Colors
StartColor = (True, {'red': '16', 'green': '135', 'blue': '151'})
TrainButtonColor = (True, {'red': '254', 'green': '255', 'blue': '254'})
LeaguesColor = (True, {'red': '255', 'green': '255', 'blue': '255'})
UsePartyColor = (True, {'red': '114', 'green': '213', 'blue': '157'})
XButtonColor = (True, {'red': '29', 'green': '134', 'blue': '150'})


def tap(x,y):
    device.touch(1, 1, x, y) 
    device.accurate_usleep(20000)
    device.touch(0, 1, x, y) 

def pause(milsec):
    device.accurate_usleep(milsec)

def Press(Scan,Button,Color):
    pressed = 0
    
    bx = int(Button[0])
    by = int(Button[1])
    
    sx = int(Scan[0])
    sy = int(Scan[1])
    
    print("Looking for Button")
   
    while 1:
        print("Looking for Button")
        result = device.pick_color(sx,sy)
        if result == Color:
            print ("Found Button! \n Pressing!")
            tap(bx,by)
            pressed = 1
            pause(500000)
              
        if result != Color and pressed:
            print("Button Pressed?")
            break
        pause(500000) 

def Attack():
    pressed = 0
    
    x = int(XButton[0])
    y = int(XButton[1])
    
    result = device.pick_color(x,y)

    print("Looking for Button")
   
    while 1:
        result = device.pick_color(x,y)
        pause(500000)
        if result == XButtonColor:
                pause(500000)
                print ("Found Button! \n Pressing!")
                tap(x,y)
                pressed = 1
                pause(500000)
        if result != XButtonColor and pressed:
                print("Button Pressed?")
                break
        
        tap(375,650)
    
        

def battle():   
    rand = random.randint(0,2)
    if rand == 0:
        print("vs. Blanche")
        Press(StartArea,Blanche,StartColor)
    elif rand == 1:
        print("vs. Candela")
        Press(StartArea,Candela,StartColor)
    elif rand == 2:
        print("vs. Spark")
        Press(StartArea,Spark,StartColor)

    Press(TrainButton,TrainButton,TrainButtonColor)
    Press(League,League,LeaguesColor)
    Press(UseParty,UseParty,UsePartyColor)
    Attack()
    
def chooseLeague():
    print ('1 -- Great' )
    print ('2 -- Ultra' )
    print ('3 -- Master' )
    
    option = int(input("Choose League: "))
           
    global League
    if option == 1:
        print("Great")
        League = (375,600)
    elif option == 2:
        print("Ultra")
        League = (375,800)
    elif option == 3:
        print("Master")
        League = (375,1000)
    

def start():
    print("Starting Train Bot by Misl3d")
    train = 0
    chooseLeague()   
    maxTrain = int(input("How many Train Battles? \n"))
    while maxTrain > train:
        train += 1 
        print("\n Training #" + str(train))
        battle()
    print("\n Training Complete!")    


start()
exit() 
