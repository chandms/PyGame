from random import *
import turtle as tt

from TurtleGames.base import vector

def value():
    # generate value [-5.-3] to [3,5]
    return (3+random()*2)*choice([-1,1])

ball = vector(0,0)
aim = vector(value(),value())

def draw():
    ball.move(aim)
    x = ball.x
    y = ball.y

    if x<-200 or x>200:
        aim.x = -aim.x
    if y<-200 or y>200:
        aim.y = -aim.y
    tt.clear()
    tt.goto(x,y)
    tt.dot(10,'blue')
    tt.ontimer(draw,50)



tt.setup(420,420,370,0)
tt.hideturtle()
tt.tracer(False)
draw()
tt.done()
