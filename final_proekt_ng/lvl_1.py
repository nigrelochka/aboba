# -*- coding: utf-8 -*-
fon1=0
pr=0
pr2=0
ch1=0
def lvlOne(y):
    global fon1,pr,pr2,ch1
    background(0)
    fon1=loadImage("fon1.jpg")
    pr=loadImage("pr1.png")
    pr2=loadImage("pr2.png")
    ch1=loadImage("sk11.png")
    image(fon1,0,0,900,700)
    strokeWeight(3)
    line(0,600,1000,600)
    image(ch1,100,y,170,100)
