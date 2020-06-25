from random import *
import turtle as tt

from TurtleGames.base import line

def draw():
    # draw maze
    tt.color('black')
    tt.width(5)

    for x in range(-200,200,40):
        for y in range(-200,200,40):
            if random()>0.5:
                line(x,y,x+40,y+40)
            else:
                line(x,y+40,x+40,y)
    tt.update()

def tap(x,y):
    # draw line
    if abs(x)>198 or abs(y)>198:
        tt.up()
    else:
        tt.down()
    tt.width(2)
    tt.color('red')
    tt.goto(x,y)
    tt.dot(4)

tt.setup(420,420,370,0)
tt.hideturtle()
tt.tracer(False)
draw()
tt.onscreenclick(tap)
tt.done()


