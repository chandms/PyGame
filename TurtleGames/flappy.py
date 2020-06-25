from random import *
from turtle import *

from TurtleGames.base import vector

bird = vector(0,0)
balls = []
all=[]
dc ={}
count=1
score =0

def tap(x,y):
    up = vector(0,30)
    bird.move(up)


def inside(point):
    return -200<  point.x <  200 and -200 < point.y <200

def draw(alive):
    # draw screen object
    clear()
    up()
    goto(bird.x,bird.y)
    down()
    if(alive):
        dot(10,'green')
    else:
        dot(10,'red')

    for ball in balls:
        up()
        goto(ball.x,ball.y)
        down()
        dot(20,'black')
    update()


def move():
    global score
    global count

    bird.y -=5
    for ball in balls:
        ball.x -=3
    for ball in all:
        ball.x -=3
    if randrange(10) == 0:
        y = randrange(-199,199)
        ball = vector(199,y)
        balls.append(ball)
        all.append(ball)
        dc[count]=0
        count +=1
    while len(balls)>0 and not inside(balls[0]):
        balls.pop(0)
    if not inside(bird):
        draw(False)
        up()
        goto(0,0)
        down()
        write('Score {} '.format(score),font=['Arial',14,'bold'])
        return
    for ball in balls:
        if (abs(ball-bird)<15):
            draw(False)
            up()
            goto(0, 0)
            down()
            write('Score {} '.format(score), font=['Arial', 14, 'bold'])
            return
        else:
            #print(ball.x,bird.x,ball.x-bird.x)
            if ball in all:
                i=all.index(ball)
                #print("i ",i, ball.x,ball.y)
                if(dc[i+1]==0):
                    if(bird.x - ball.x >15):
                        score+=1
                        dc[i+1]=1
    draw(True)
    ontimer(move,50)

setup(420,420,370,0)
hideturtle()
tracer(False)
onscreenclick(tap)
move()
done()

