#Initialize Program
import pygame
import math
import random
pygame.init()

#Create Window
screenwid = 1100
screenhei = 500
win = pygame.display.set_mode((screenwid,screenhei))
pygame.display.set_caption('Asteroid Game')

#Create Class for Ship
class player(object):
    def __init__(self, x,y,width,vel,direction,dx,dy):
        self.x = x
        self.y = y
        self.width = width
        self.vel = vel
        self.direction = direction
        self.dx = dx
        self.dy = dy

    def draw(self, win):
        pygame.draw.polygon(win, (255,255,255), [(self.x,self.y),(self.x+self.width*math.cos(self.direction+ ((5/6)*math.pi)),self.y+self.width*math.sin(self.direction+ ((5/6)*math.pi))),(self.x+self.width*math.cos(self.direction+ ((7/6)*math.pi)),self.y+self.width*math.sin(self.direction+ ((7/6)*math.pi)))],2)

#Create Class for Bullets
class projectile(object):
    def __init__(self, x,y,direction,vel):
        self.x = x
        self.y = y
        self.direction = direction
        self.vel = vel

    def draw(self,win):
        pygame.draw.circle(win, (255,255,255), [round(self.x),round(self.y)],5,1)

#Create Class for Asteroid
class roid(object):
    def __init__(self,x,y,width,vel,direction):
        self.x = x
        self.y = y
        self.width = width
        self.vel = vel
        self.direction = direction
    
    def draw(self,win):
        pygame.draw.circle(win, (255,255,255), [round(self.x),round(self.y)],self.width)

#Game Initialization
run = True
ship = player(screenwid/2,screenhei/2,15,2,0,0,0)
bullets = []
roids = []
score = 0

#Main Game Loop
while run:
    #Get Font for Text
    font = pygame.font.SysFont('comicsans', 30, True)
    #Set Time Delay
    pygame.time.delay(10)
    #Check if Game is Stopped
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Move Bullets
    for bullet in bullets:
        if bullet.x < screenwid and bullet.x > 0 and bullet.y > 0 and bullet.y < screenhei:
            bullet.x += bullet.vel*math.cos(bullet.direction)
            bullet.y += bullet.vel*math.sin(bullet.direction)
            
        else:
            bullets.remove(bullet)
    
    #Move Asteroids and Check Detection with Bullets 
    for asteroid in roids:
        if ((ship.x - asteroid.x)**2 + (ship.y - asteroid.y)**2)**(0.5) <= asteroid.width + ship.width:
            if ((ship.x - asteroid.x)**2 + (ship.y - asteroid.y)**2)**(0.5) <= asteroid.width + 2 or ((ship.x+ship.width*math.cos(ship.direction+ ((5/6)*math.pi)) - asteroid.x)**2 + (ship.y+ship.width*math.sin(ship.direction+ ((5/6)*math.pi)) - asteroid.y)**2)**(0.5) <= asteroid.width + 2 or ((ship.x+ship.width*math.cos(ship.direction+ ((7/6)*math.pi)) - asteroid.x)**2 + (ship.y+ship.width*math.sin(ship.direction+ ((7/6)*math.pi)) - asteroid.y)**2)**(0.5) <= asteroid.width + 2:
                ship.x = screenwid/2
                ship.y = screenhei/2
                score = 0
        if asteroid.x <= screenwid and asteroid.x >= 0 and asteroid.y >= 0 and asteroid.y <= screenhei:
            asteroid.x += asteroid.vel*math.cos(asteroid.direction)
            asteroid.y += asteroid.vel*math.sin(asteroid.direction)
            for bullet in bullets:
                if ((bullet.x - asteroid.x)**2 + (bullet.y - asteroid.y)**2)**(0.5) <= asteroid.width + 5:
                    roids.remove(asteroid)
                    bullets.remove(bullet)
                    score += 1
            
            
        else:
            roids.remove(asteroid)
    

    #Creates New Asteroids
    if len(roids) < 50:
        randside = random.randint(0,1)
        if randside == 0:
            roids.append(roid(random.randint(0,1)*screenwid, random.randint(0,screenhei), random.randint(6,13),random.randint(2,7),random.random()*2*math.pi))
        else:
            roids.append(roid(random.randint(0,screenwid), random.randint(0,1)*screenhei, random.randint(6,13),random.randint(2,7),random.random()*2*math.pi))




    #Controls
    #Space for Bullets
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if len(bullets) < 100 and spacekeypress == False:
            bullets.append(projectile(ship.x,ship.y,ship.direction,10))
        spacekeypress = True
    else:
        spacekeypress = False

    #Turn and Moves
    if keys[pygame.K_e]:
        ship.direction += (math.pi/12)
    if keys[pygame.K_q]:
        ship.direction -= (math.pi/12)
    if keys[pygame.K_a]:
        ship.dx -= ship.vel
    if keys[pygame.K_d]:
        ship.dx += ship.vel
    if keys[pygame.K_w]:
        ship.dy -= ship.vel
    if keys[pygame.K_s]:
        ship.dy += ship.vel

    #Update Ship Position
    ship.x += ship.dx
    ship.y += ship.dy

    #Wall Collision with Ship
    if ship.x + ship.width > screenwid:
        ship.dx = 0
        ship.x = screenwid - ship.width
    if ship.x - ship.width < 0:
        ship.dx = 0
        ship.x = ship.width
    if ship.y + ship.width > screenhei:
        ship.dy = 0
        ship.y = screenhei - ship.width
    if ship.y - ship.width< 0:
        ship.dy = 0
        ship.y = ship.width

    

    #Constant Ship Slowdown
    ship.dx *= 0.9
    ship.dy *= 0.9

    #Draw New Screen and Update and Update Text
    win.fill((0,0,0))
    text = font.render('Score: ' + str(score),1,(255,255,255))
    win.blit(text,(screenwid/2 - 40, screenhei*0.05))
    ship.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    for asteroid in roids:
        asteroid.draw(win)
    pygame.display.update()