#Trade Bot 2.0
from zxtouch.client import zxtouch 
from zxtouch.touchtypes import *
import time

#DEVICE IP 
device = zxtouch("192.168.1.177")

#Button Coordinates
#Button Coordinates
PokemonSelect = ("50", "450")
EvoButton = ("200", "1265")
ConfirmButton = ("375", "830")
XButton =  ("375", "1230")

#Button Colors
PokemonSelectColor = (True, {'red': '253', 'green': '255', 'blue': '253'})
EvoButtonColor = (True, {'red': '116', 'green': '214', 'blue': '157'})
ConfirmButtonColor = (True, {'red': '114', 'green': '213', 'blue': '157'})
XButtonColor = (True, {'red': '29', 'green': '134', 'blue': '150'})

def tap(x,y):
    device.touch(1, 1, x, y) 
    device.accurate_usleep(20000)
    device.touch(0, 1, x, y) 

def pause(milsec):
    device.accurate_usleep(milsec)

def Press(Button, Color):
    x = int(Button[0])
    y = int(Button[1])
    result = device.pick_color(x,y)

    print("Looking for Button")
   
    while 1:
        result = device.pick_color(x,y)
        if result == Color:
                pause(500000)
                print ("Found Button! \n Pressing!")
                tap(x,y)
                pause(1000000)
                break
def evolve():
    Press(PokemonSelect, PokemonSelectColor)
    Press (EvoButton, EvoButtonColor)    
    Press (ConfirmButton, ConfirmButtonColor)
    Press (XButton, XButtonColor)


def start():
    print("Starting Evolve Bot by Misl3d")
    evolves = 0
    maxEvo = int(input("How many evolutions? \n"))
    while maxEvo > evolves:
        evolves += 1 
        print("\n Evolution #" + str(evolves))
        evolve()
    print("\n Trading Complete!")    


start()
exit() 
