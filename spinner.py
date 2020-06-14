from turtle import *
from random import *

from base import vector

state ={'turn':0}

def spinner():
    clear()
    angle = state['turn']/10
    right(angle)

    forward(100)
    dot(120,'red')
    back(100)
    right(120)

    forward(100)
    dot(120,'green')
    back(100)
    right(120)
    forward(100)

    dot(120,'blue')
    back(100)
    right(120)

    update()

def animate():
    if state['turn']<0:
        state['turn']-=1
    spinner()
    ontimer(animate,120)

def flick():
    state['turn']+=10

setup(420,420,370,0)
hideturtle()
tracer(False)
width(20)

onkey(lambda :flick(),'space')
listen()
animate()
done()