from snezinka import snez

l=1
h=1
def setup():
    size(700,700)
def draw():
    global l,h
    snez(l,h,5)
    l=l+1
    h=h+1

    
    
