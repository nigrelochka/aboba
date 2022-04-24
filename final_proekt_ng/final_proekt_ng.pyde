from lvl_1 import lvlOne
ch=0
ch2=0
ch3=0
f0n2=0
def setup():
    size(900,700)
    global ch,ch2,ch3,fon2
    ch=loadImage("sk1.png")
    ch2=loadImage("sk2.png")
    ch3=loadImage("sk3.png")
    fon2=loadImage("fon2.jpg")
def draw():
    global ch,ch2,ch3,fon2,fon1
    lvlOne()
    image(ch,100,400,170,100)    
