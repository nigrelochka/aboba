# -*- coding: utf-8 -*-
ch=0
ch2=0
ch3=0
fon11=0
f0n2=0
strt=0
lvl=0
def start():
    global ch,ch2,ch3,fon2,fon11,strt,lvl
    ch=loadImage("sk1.png")
    ch2=loadImage("sk2.png")
    ch3=loadImage("sk3.png")
    fon2=loadImage("fon2.jpg")
    fon11=loadImage("fon11.jpg")
    strt=loadImage("start.png")
    image(fon11,0,0,900,700)
    image(ch,400,500,170,100)
    image(strt,320,300,250,150)   
    textAlign(CENTER)
    textSize(30)
    fill(0)
    text(u"Привет! Это финальная часть игры про черепашку",450,200+20) 
    text(u"Сегодня черепашка наконец-то сможет покинуть пляж",450,240+20+5) 
    text(u"Твоя цель помочь ей в этом, удачи!",450,280+20+5)
    textSize(15)
    text(u"Нажмите для старта",450,410)
