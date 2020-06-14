from random import *
import turtle as tt

from base import vector

ball= vector(-200,-200)
speed = vector(0,0)
targets=[]
specialBalls=[]
curIncrement =200
FONT = ("Arial", 14, "bold")
score =0
blueBall=0
yellowBall=0

def inside(xy):
    return -200 < xy.x <200 and -200 <xy.y < 200

def tap(x,y):
    global curIncrement
    # respond to the screen
    if not inside(ball):
        ball.x =-199
        ball.y =-199
        speed.x = (x+curIncrement)/25
        speed.y = (y+curIncrement)/25

def move():
    # movement of ball and targets
    global score
    global curIncrement
    global blueBall
    global yellowBall
    if randrange(200) == 0:
        x=randrange(-150,150)
        specialBall = vector(x,200)
        specialBalls.append(specialBall)

    if randrange(40) == 0:
        y= randrange (-150,150)
        target = vector(200,y)
        targets.append(target)

    for target in targets:
        target.x -=0.5
    for specialBall in specialBalls:
        specialBall.y-=0.5

    if(inside(ball)):
        ball.y -=0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if (abs(target-ball)>13):
            targets.append(target)
        else:
            score+=10
            blueBall+=1
    spDupe = specialBalls.copy()
    specialBalls.clear()
    for specialBall in spDupe:
        if(abs(specialBall-ball)>13):
            specialBalls.append(specialBall)
        else:
            score+=15
            curIncrement+=10
            yellowBall+=1
    draw()

    for target in targets:
        if not inside(target):
            tt.penup()
            tt.goto(-80,0)
            tt.write("Your Score {} \n Blue Balls :{} \n Yellow Balls :{}".format(score,blueBall,yellowBall), font=FONT)
            return
    tt.ontimer(move,50)



def draw():
    # draw ball and targets
    tt.clear()
    for specialBall in specialBalls:
        tt.goto(specialBall.x,specialBall.y)
        tt.dot(30,'yellow')

    for target in targets:
        tt.goto(target.x,target.y)
        tt.dot(20,'blue')

    if( inside(ball)):
        tt.goto(ball.x,ball.y)
        tt.dot(10,'red')




tt.setup(420,420,370,0)
tt.hideturtle()
tt.up()
tt.tracer(False)
tt.onscreenclick(tap)
move()
tt.done()

