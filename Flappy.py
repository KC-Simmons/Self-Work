import pygame
import random

pygame.init()

#Initialize Pygame
screenwid = 600
screenhei = 600
win = pygame.display.set_mode((screenwid,screenhei))
pygame.display.set_caption('FlappyBird')

class bird(object):
    def __init__(self):
        self.y = screenhei/2
        self.x = 50
        self.dy = 0
        self.color = 1

    def draw(self, win):
        pygame.draw.circle(win, (225,225*self.color,0), [round(self.x),round(self.y)], 9)

class pipe(object):
    def __init__(self, top, length):
        self.top = top
        self.x = screenwid
        if self.top:
            self.y = 0
        else:
            self.y = screenhei - length
        self.length = length

    def draw(self, win):
        pygame.draw.rect(win,(50,205,50), (self.x,self.y, 50, self.length))


run = True
spacepress = False

player = bird()
min_dy = -5
openwidth = 45
hitcheck = False

pipes = []
hits = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if not(spacepress):
            player.dy = 7
        spacepress = True
    else:
        spacepress = False
    
    #Check Through Pipes

    #Check if Pipe is too close to make new one
    tooClose = False
    hitcheck = False
    for obj in pipes:
        if obj.x >= (2*screenwid)/3:
            tooClose = True
        if obj.x <= -50:
            pipes.remove(obj)
        if player.x + 9 > obj.x and player.x - 9< obj.x + 50:
            if obj.top:
                if player.y - obj.length < 9:
                    if not(hitcheck):
                        hits += 1
                    hitcheck = True
            if not(obj.top):
                if (player.y - obj.y) > -9:
                    if not(hitcheck):
                        hits += 1
                    hitcheck = True


                

        
        #Pipe Passive Movement
        obj.x += -2



    #Make New Pipes
    if len(pipes) < 6 and tooClose == False:
        randopen  = random.randint(150, screenhei-150)
        pipes.append(pipe(True, randopen - openwidth))
        pipes.append(pipe(False,screenhei - randopen - openwidth))

    #Bird Passive Movement
    if player.dy >= min_dy:
        player.dy -= 0.3
    player.y += -player.dy
    
    if hitcheck:
        player.color = 0
    else:
        player.color = 1

    if player.y - 9 < 0:
        player.y = 9
    if player.y > screenhei - 9:
        player.y = screenhei - 9

    win.fill((135,206,235))

    
    for obj in pipes:
        obj.draw(win)
    player.draw(win)
    pygame.display.update()

print(hits)