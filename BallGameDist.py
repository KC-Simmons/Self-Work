#Initialize Window
import turtle
import random
import time
import math
import matplotlib.pyplot as plt

wn=turtle.Screen()
wn.title('Squares vs. Circle')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

#Get Starting Time
starttime = time.time()
timelimit = 15
currtime = 14

#Score
score = 0
scoredist = []


#FirstChar(Ball)
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)


#SecondChar(Square)
square = turtle.Turtle()
square.speed(0)
square.shape('square')
square.color('red')
square.penup()
square.goto(100,0)
square.dx = 8
square.dy = 8

#Text
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('0 Squares Caught - 15 Seconds Remaining', align='center', font=('Courier',24,'normal'))

#Function for Ball Move
ball.dx = 0
ball.dy = 0

def ballup():
    ball.dy += 2

def balldown():
    ball.dy -= 2

def ballright():
    ball.dx += 2

def ballleft():
    ball.dx -= 2

def reset():
    global score
    scoredist.append(score)
    score = 0
    global starttime
    starttime = time.time()
    global currtime
    currtime = 14
    ball.goto(0,0)
    square.goto(100,0)
    square.dx = 8
    square.dy = 8
    ball.dx = 0
    ball.dy = 0
    pen.clear()
    pen.write('0 Squares Caught - 15 Seconds Remaining', align='center', font=('Courier',24,'normal'))
    print(scoredist)



#DummyAI
global AISwitch
AISwitch = False

def AITurnOn():
    global AISwitch
    if AISwitch == False:
        AISwitch = True
    else:
        AISwitch = False



#Keyboard Binding
wn.listen()
wn.onkeypress(ballup,'w')
wn.onkeypress(balldown,'s')
wn.onkeypress(ballleft,'a')
wn.onkeypress(ballright,'d')
wn.onkey(AITurnOn, 'p')
wn.onkey(reset, 'n')

#Main Game Loop
while True:
    wn.update()

    #Move the Square
    square.setx(square.xcor() + (square.dx*((score+5)*0.05)))
    square.sety(square.ycor() + (square.dy*((score+5)*0.05)))
    square.right(2+score)

    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.dx > 0:
        ball.dx -= 0.08
    if ball.dx < 0:
        ball.dx += 0.08
    if ball.dy > 0:
        ball.dy -= 0.08
    if ball.dy < 0:
        ball.dy += 0.08
    if ball.dy < 0.08 and ball.dy > -0.08:
        ball.dy = 0
    if ball.dx < 0.08 and ball.dx > -0.08:
        ball.dx = 0
    
    #Dummy AI Implement
    if AISwitch == True:
        if ball.ycor() > square.ycor():
            balldown()
        else:
            ballup()
        if ball.xcor() > square.xcor():
            ballleft()
        else:
            ballright()
    


    #Square Border Checking
    if square.ycor() > 290:
        square.sety(290)
        square.dy *= -1
    if square.ycor() < -280:
        square.sety(-280)
        square.dy *= -1
    if square.xcor() > 380:
        square.setx(380)
        square.dx *= -1
    if square.xcor() < -390:
        square.setx(-390)
        square.dx *= -1

    #Ball Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
    if ball.xcor() > 380:
        ball.setx(380)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    #Find Time Remaining and Update Time
    timeremain = math.ceil(timelimit - (time.time() - starttime))
    if timeremain <= currtime:
        pen.clear()
        pen.write('{} Squares Caught - {} Seconds Remaining'.format(score, timeremain), align='center', font=('Courier',24,'normal'))
        currtime -= 1


    #Square Ball Collision
    if ((ball.xcor() - square.xcor())**2 + (ball.ycor() - square.ycor())**2)**(1/2) < 24.3:
        square.setx(-390 + (random.random()*(770)))
        square.sety(-280 + (random.random()*(570)))
        score += 1
        pen.clear()
        pen.write('{} Squares Caught - {} Seconds Remaining'.format(score, timeremain), align='center', font=('Courier',24,'normal'))
        

    #Find Slope Between Ball and Square
    if square.xcor()-ball.xcor() != 0:
        slope = (square.ycor()-ball.ycor())/(square.xcor()-ball.xcor())

    #Reset Game
    if (time.time() - starttime) > timelimit:
        reset()




    


