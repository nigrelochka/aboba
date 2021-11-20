x = 150
y = 300
k = 350
u = 150
l = 350
z = 450
def setup():
    size(600,600)
def draw():
    global x 
    global y
    global k
    global u
    global l
    global z
    triangle(x,k,y,u,z,l)
    x = x - 1 
    k = k + 1
    u = u - 1
    l = l + 1
    z = z + 1  
