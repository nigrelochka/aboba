x=0
x2=0
x3=0
x4=0
x5=0
i=0
x1=0
x6=0
list1=[]
def setup():
    size(600,600)
    global x,x2,x3,x4,x5,x6,x1,list1
    x = loadImage("l1.png")
    x2 = loadImage("l2.png")
    x3 = loadImage("l3.png")
    x4 = loadImage("l4.png")
    x5 = loadImage("l5.png")
    x1=loadImage("l6.png")
    x6=loadImage("l7.png")
    list1.append(x)
    list1.append(x2)
    list1.append(x3)
    list1.append(x4)
    list1.append(x5)
    list1.append(x6)
    list1.append(x1)
def draw(): 
    global x,x2,x3,x4,x5,list1,i 
    if i>5:
        i=i-1
    if i<0:
        i=i+1   
def keyPressed():
    global list1,i
    if key == CODED:
        if keyCode == DOWN: 
            i=i-1
            image(list1[i],0,0,600,600)
    if key == CODED:
        if keyCode == UP: 
            i=i+1             
            image(list1[i],0,0,600,600)
