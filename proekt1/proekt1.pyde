x = 0
y = 0
z = 0
d = 50
def setup():
    size(800,800)
    frameRate(20)

def draw():
    global x,y,z,d
    push()
    translate(400,400) 
    rotate(radians(z))
    fill(random (0,255),random(0,255),random(0,255))
    ellipse(x,y,d,d)
    x = x + 2
    y = y + 2
    z = z + 100
    d = d + 1
    pop()
    

    
          
    
     
        
