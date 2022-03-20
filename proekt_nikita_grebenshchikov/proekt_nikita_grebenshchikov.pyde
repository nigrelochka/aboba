pole = [['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white'],
        ['white','white','white','white','white','white','white','white','white','white','white','white','white','white']]
x=0
y=40

numRyad = len(pole) 
numStolbets = len(pole[0])
def setup():
    size(700,700)
    for nRyada in range(numRyad): 
        for nStolbtsa in range(numStolbets):
            if pole[nRyada][nStolbtsa] == 'white':
                fill(255)  
def draw():
    
    global pole, finRyad, finStolbets
    for nRyada in range(numRyad): 
        for nStolbtsa in range(numStolbets):
            #if mouseButton==LEFT:
                #if mouseX>nStolbtsa*50 and mouseX<nStolbtsa*50+50 and mouseY>nRyada*50 and mouseY<nRyada*50+50:
                    #pole[nRyada][nStolbtsa] == 'black'
                    #fill(0)
                    #rect(nStolbtsa*50,nRyada*50,50,50)
    
            rect(nStolbtsa*50,nRyada*50,50,50)
