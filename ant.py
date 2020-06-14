from random import *
import turtle as tt

from base import vector

ant = vector(0,0)
aim = vector(2,0)

def wrap(value):
    return value

def draw():
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)
    print('ant {}{}'.format(ant.x,ant.y))
    print('aim {}{}'.format(aim.x, aim.y))
    aim.move(random()-0.5)
    aim.rotate(random()*10-5)
    tt.clear()

    tt.goto(ant.x,ant.y)
    tt.dot(10,'blue')
    if tt.running:
        tt.ontimer(draw,1000) # if running is true , draw function is called after each 100 ms

tt.setup(420,420,370,0)
# to make turtle screen invisible
tt.hideturtle()
#No dely for animation on/off or update
tt.tracer(False)
tt.up()
tt.running = True
draw()
tt.done()






