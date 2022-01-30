z=15
h=8
g=1
l=(random(0,255))
def setup():
    size(600,600)
    global f,dls,dl
    f=(random(0,255))
    dls=(random(0,255))
    dl=(random(0,255))
def draw():
    global z,h,g,l
    
    global f,dls,dl
    translate(300,300)
    # f=(random(0,255))wc
    # dls=(random(0,255))
    # dl=(random(0,255))
    h=h+g
    z=z+g
    if z > 80:
        g=-1
    if z < 1:
        g=1    
    for x in range(500):
        fill(f,dl,dls)
        rotate(radians(h))
        ellipse(100,100,z,z)
def keyPressed(): 
    global f,dls,dl   
    if key == 'w' or key == 'W' or key == u'ц' or key == u'Ц':
      
        f=197
        dl=101
        dls=216
    if key == DELETE: 
       background(255)    
    if key == 'A' or key == 'A' or key == u'ф' or key == u'Ф':
      f=101
      dl=216
      dls=121
    if key == 'F' or key == 'f' or key == u'а' or key == u'А':
      
      f=236
      dl=240
      dls=56 
    if key == 'B' or key == 'b' or key == u'И' or key == u'и':
      
      f=56
      dl=118
      dls=240
    if key == 'V' or key == 'v' or key == u'М' or key == u'м':  
       f=240
       dl=56
       dls=56 
    if key == 'z' or key == 'Z' or key == u'я' or key == u'Я':
       f=(random(0,255))
       dls=(random(0,255))
       dl=(random(0,255))  


