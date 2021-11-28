x = 45
y = 0
x1 = -20
x2 = 20
x3 = 48
z = 150
z1 = 120
z2 = 180
z3 = 100
z4 = 200

def setup():
    size(800,800)
    
def draw():
    frameRate(2)
    background(114,187,250)
    push()
    noStroke()
    fill(54,118,206)
    rect(0,400,900,70)
    pop()
    push()
    fill(240,228,99)
    strokeWeight(1)
    ellipse(700,100,100,100)
    pop()
    push()
    fill(240,228,99)
    noStroke()
    rect(0,470,800,800)
    pop()
    translate(200,0)
    push()
    global x,y, x1, x2,x3, z,z1,z2,z3,z4
    fill(47,211,133)
    strokeWeight(3)
    ellipse(x1,520,30,30)
    ellipse(x1,580,30,30)
    ellipse(x2,580,30,30)
    ellipse(x2,520,30,30)
    ellipse(x,550,40,40)
    ellipse(y,550,80,80)
    push()
    strokeWeight(5)
    point(x3,543)
    point(x3,558)
    pop()
    y = y + 2
    x = x + 2
    x1 = x1 + 2
    x2 = x2 + 2
    x3 = x3 + 2
    pop()
    translate(150,50)
    fill(47,211,133)
    strokeWeight(3)
    ellipse(x1,520,30,30)
    ellipse(x1,580,30,30)
    ellipse(x2,580,30,30)
    ellipse(x2,520,30,30)
    ellipse(x,550,40,40)
    ellipse(y,550,80,80)
    push()
    strokeWeight(5)
    point(x3,543)
    point(x3,558)
    y = y + 2
    x = x + 2
    x1 = x1 + 2
    x2 = x2 + 2
    x3 = x3 + 2
    pop()

    translate(-100,120)
    fill(47,211,133)
    strokeWeight(3)
    ellipse(x1,520,30,30)
    ellipse(x1,580,30,30)
    ellipse(x2,580,30,30)
    ellipse(x2,520,30,30)
    ellipse(x,550,40,40)
    ellipse(y,550,80,80)
    push()
    strokeWeight(5)
    point(x3,543)
    point(x3,558)
    pop()
    y = y + 2
    x = x + 2
    x1 = x1 + 2
    x2 = x2 + 2
    x3 = x3 + 2
    translate(-150,-50)
    fill(47,211,133)
    strokeWeight(3)
    ellipse(x1,520,30,30)
    ellipse(x1,580,30,30)
    ellipse(x2,580,30,30)
    ellipse(x2,520,30,30)
    ellipse(x,550,40,40)
    ellipse(y,550,80,80)
    push()
    strokeWeight(5)
    point(x3,543)
    point(x3,558)
    pop()
    y = y + 2
    x = x + 2
    x1 = x1 + 2
    x2 = x2 + 2
    x3 = x3 + 2
    translate(-100,-100)
    fill(47,211,133)
    strokeWeight(3)
    ellipse(x1,520,30,30)
    ellipse(x1,580,30,30)
    ellipse(x2,580,30,30)
    ellipse(x2,520,30,30)
    ellipse(x,550,40,40)
    ellipse(y,550,80,80)
    push()
    strokeWeight(5)
    point(x3,543)
    point(x3,558)
    pop()
    y = y + 2
    x = x + 2
    x1 = x1 + 2
    x2 = x2 + 2
    x3 = x3 + 2
    translate(-50,170)
    fill(47,211,133)
    strokeWeight(3)
    ellipse(x1,520,30,30)
    ellipse(x1,580,30,30)
    ellipse(x2,580,30,30)
    ellipse(x2,520,30,30)
    ellipse(x,550,40,40)
    ellipse(y,550,80,80)
    push()
    strokeWeight(5)
    point(x3,543)
    point(x3,558)
    pop()
    y = y + 2
    x = x + 2
    x1 = x1 + 2
    x2 = x2 + 2
    x3 = x3 + 2
    push()
    fill(255)
    noStroke()
    ellipse(z,-50,150,70)
    ellipse(z,-50,50,90)
    ellipse(z1,-50,50,80)
    ellipse(z2,-50,50,80)
    ellipse(z3,-50,50,70)
    ellipse(z4,-50,50,70)
    ellipse(z,-50,170,60)
    
    translate(230,-50) 
    
    ellipse(z,-50,150,70)
    ellipse(z,-50,50,90)
    ellipse(z1,-50,50,80)
    ellipse(z2,-50,50,80)
    ellipse(z3,-50,50,70)
    ellipse(z4,-50,50,70)
    ellipse(z,-50,170,60)
    
    translate(210,70)
    
    ellipse(z,-50,150,70)
    ellipse(z,-50,50,90)
    ellipse(z1,-50,50,80)
    ellipse(z2,-50,50,80)
    ellipse(z3,-50,50,70)
    ellipse(z4,-50,50,70)
    ellipse(z,-50,170,60)
    z = z - 1
    z1 = z1 - 1
    z2 = z2 - 1
    z3 = z3 - 1
    z4 = z4 -1
    pop()
    push()
    translate(100,-200)
    strokeWeight(10)
    stroke(113,70,70)
    line(300,470,350,270)
    stroke(0)
    strokeWeight(1)
    fill(242,125,125)
    triangle(210,240,375,170,470,310)
    pop()
    

    
          
    
     
        
