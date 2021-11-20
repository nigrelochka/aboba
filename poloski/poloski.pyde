x = 600
y = 0

def setup():
    size(600,600)
def draw():
    global x 
    global y
    stroke(random (0,255),random (0,255),random (0,255))
    strokeWeight(10) 
    line(200,0,200,y)
    line(400,600,400,x)
    y = y + 1
    x = x - 1
