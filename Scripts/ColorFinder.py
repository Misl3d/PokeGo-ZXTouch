
from zxtouch.client import zxtouch 
from zxtouch.touchtypes import *
import time


devicenum = (input("Device IP: "))


def ColorFinder(device, x, y):
    result = device.pick_color(x,y)
    print(result)

device = zxtouch(str(devicenum))

while 1:
    xcor = int(input("X: "))
    ycor = int(input("Y: "))
    ColorFinder(device, xcor, ycor)


