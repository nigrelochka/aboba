x = 30
y = 0

def setup():
    size(800,800)
    frameRate(20)

def draw():
    background(114,187,250)
    translate(200,0)
    global x,y
    ellipse(y,550,80,60)
    push()
    noStroke()
    ellipse(x,530,45,40)
    pop()
    y = y + 2
    x = x + 2
    

    
          
    
     
        
