import random
import pygame
import numpy as np 

pygame.init()

#Initialize Pygame
screenwid = 600
screenhei = 600
win = pygame.display.set_mode((screenwid,screenhei))
pygame.display.set_caption('Line Guess')

#Create Random Line
realm = random.random() - 0.5
realb = random.randint(-5,5)

def sigmoid(x):
    return 1/(1+ np.exp(-x))

#Activiation Function
def activationfunc(x):
    if x >= 0:
        return 1
    else:
        return -1

#Create Points
class point(object):
    def __init__(self):
        self.x = random.randint(0, screenwid)
        self.y = random.randint(0,screenhei)
        if ((realm * self.x) + realb) + 300 >= self.y:
            # -1=PTBelowLine, 1=PTAboveLine
            self.above = 1
        else:
            self.above = -1
    
    def draw(self,win):
        pygame.draw.circle(win,[0,127 +(127*self.above),127+(127*(-self.above))],(self.x,self.y),5)

#Create Random Weights
weights = [random.random() - 0.5, random.randint(-5,5), random.randint(-500,500)]


run = True
points = []
tpress = False
trainingset = []
iterations = 0
maxpoints = 500



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()

    while len(points) < maxpoints:
        points.append(point())

    if keys[pygame.K_t]:
        runningError = 0
        trainingset = []
        for element in points:
            
            trainingset.append([(element.x - 300)/300,(element.y - 300)/300,1,element.above])
        for datum in trainingset:
            guess = activationfunc(weights[0]*datum[0] + weights[1]*datum[1] + weights[2]*datum[2])
            error = datum[3] - guess
            runningError += abs(error)
            if error != 0:
                for i in range(0, len(weights)):
                    weights[i] +=  (error*datum[i]) * 0.1
        print(runningError)
        if runningError == 0:
            runningCheck = 0
            for element in points:
                if element.y >= (-(weights[0]/weights[1])*element.x) -(weights[2]/weights[1]) + 300  and element.above == -1:
                    runningCheck += 1
                elif element.y <= (-(weights[0]/weights[1])*element.x) -(weights[2]/weights[1]) + 300  and element.above == 1:
                    runningCheck += 1
            print('Running Check: ' + str(runningCheck) + '/' + str(maxpoints))
    

    if keys[pygame.K_SPACE]:
        iterations +=1
        print('Crash Test: ' + str(iterations))


    win.fill((0,0,0))
    if weights[1] != 0:
        pygame.draw.line(win, [255,0,0], [0,-(weights[2]/weights[1]) + 300], [screenwid, (-(weights[0]/weights[1])*screenwid) -(weights[2]/weights[1]) + 300],1)    
    pygame.draw.line(win, [255,0,255], [0,realb + 300], [screenwid, realm*screenwid + realb + 300],1)
    for element in points:
        element.draw(win)
    pygame.display.update()