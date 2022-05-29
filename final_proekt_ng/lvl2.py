fon2=0
pr2=0
pr1=0
ch1=0
x=1000
y1=470
z=0
def lvlTwo(y):
    global fon1,pr3,pr4,ch1,x,y1,z
    background(0)
    fon2=loadImage("fon2.jpg")
    pr1=loadImage("pr1.png")
    pr2=loadImage("pr2.png")
    ch1=loadImage("sk11.png")
    image(fon1,0,0,900,700)
    push()
    strokeWeight(3)
    line(0,600,1000,600)
    pop()
    image(ch1,100,y,170,100)
    image(pr1,x,y1,200,150)
    fill(255)
    rect(30,50,150,50)
    text(u"счёт",30,50)
    if x>-300:
        x=x-10
    if x<-201:
        x=1000
    z=z+10
