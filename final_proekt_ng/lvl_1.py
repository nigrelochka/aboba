# -*- coding: utf-8 -*-
fon1=0
pr3=0
pr4=0
ch1=0
x=1000
y1=470
z=0
def lvlOne(y):
    global fon1,pr3,pr4,ch1,x,y1,z
    background(0)
    fon1=loadImage("fon1.jpg")
    pr3=loadImage("pr3.png")
    pr4=loadImage("pr4.png")
    ch1=loadImage("sk11.png")
    image(fon1,0,0,900,700)
    push()
    strokeWeight(3)
    line(0,600,1000,600)
    pop()
    image(ch1,100,y,170,100)
    image(pr3,x,y1,200,150)
    fill(255)
    rect(30,50,150,50)
    text(u"счёт",30,50)
    if x>-300:
        x=x-10
    if x<-201:
        x=1000
    z=z+100

        
           
