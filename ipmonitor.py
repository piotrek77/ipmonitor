import os
import time
#import turtle
from graphics import *



adres1 = '192.168.1.1'
adres11 = '192.168.1.11'
#zolw = turtle.Turtle()
#ekran = zolw.screen
#zolw.write('test')
#ekran.clear()


win = GraphWin(width = 200, height = 200)
win.setCoords(0,100,100,0)

label1 = Text(Point(20,10), adres1)
label1.draw(win)

label11 = Text(Point(20,30), adres11)
label11.draw(win)

kontrolka1 = Circle(Point(45,9),3)
kontrolka1.setOutline('black')
kontrolka1.draw(win)
kontrolka11 = Circle(Point(45,29),3)
kontrolka11.setOutline('black')
kontrolka11.draw(win)

while True:
 resp1 = os.system("sudo ping -c 1 " + adres1)
 resp11 = os.system("sudo ping -c 1 " + adres11)
 if resp1==0:
        #print( adres1, ' UP ')
        kontrolka1.setFill('green')
 else:
        #print (adres1, ' DOWN')
        kontrolka1.setFill('red')
 if resp11==0:
        #print( adres1, ' UP ')
        kontrolka11.setFill('green')
 else:
        #print (adres1, ' DOWN')
        kontrolka11.setFill('red')
 time.sleep(1)
