from lvl_1 import *
from lvl import start
y=500
Lvl=0
def setup():
    size(900,700)
    frameRate(60)
def draw():
    global Lvl,y
    if Lvl==0:
        start()
    if Lvl==1:
        lvlOne(y)
        if keyPressed == True:
            if keyCode == SHIFT:
                if y>200:
                    y=y-15
        if keyPressed == False:
            if y<450:
                y=y+10            
      
def mouseClicked():    
    global Lvl
    if mouseX > 320 and mouseX < 570 and mouseY > 300 and mouseY < 450:
        Lvl=Lvl+1
        
