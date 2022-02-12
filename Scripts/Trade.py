#Trade Script by Misl3d
from zxtouch.client import zxtouch 
from zxtouch.touchtypes import *
import time

#DEVICE IP 
device = zxtouch("192.168.1.177")

#Button Coordinates
TradeButton = ("600", "1150")
PokemonSelect = ("50", "450")
NextButton =  ("375", "1075")
ConfirmButton = ("45", "680")
XButton =  ("375", "1230")

#Button Colors
TradeButtonColor = (True, {'red': '240', 'green': '255', 'blue': '255'})
PokemonSelectColor = (True, {'red': '253', 'green': '255', 'blue': '253'})
NextButtonColor = (True, {'red': '115', 'green': '214', 'blue': '157'})
ConfirmButtonColor = (True, {'red': '105', 'green': '208', 'blue': '146'})
XButtonColor = (True, {'red': '29', 'green': '133', 'blue': '149'})

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
def trade():
    Press(TradeButton, TradeButtonColor)
    Press(PokemonSelect, PokemonSelectColor)
    Press (NextButton, NextButtonColor)    
    Press (ConfirmButton, ConfirmButtonColor)
    Press (XButton, XButtonColor)

def start():
    print("Starting Trade Bot by Misl3d")
    trades = 0
    maxtrades = int(input("How many trades? \n"))
    while maxtrades > trades:
        trades += 1 
        print("\n Trade #" + str(trades))
        trade()
    print("\n Trading Complete!")    

start()
exit() 
