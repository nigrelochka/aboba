def snegovik(x,y,changeSize):
    push()
    translate(x,y)
    scale(changeSize)
    ellipse(0,460,100,100)
    ellipse(0,400,70,70)
    ellipse(0,350,40,40)
    line(-35,400,-70,350)
    line(35,400,70,350)
    pop()
