from turtle import *

state ={'turn' : 0}


def draw():
    clear()
    angle = state['turn']*10
    if(state['turn']>0):
        state['turn']-=1
    mode()
    setheading(0)
    up()
    goto(0,-100)
    down()
    circle(100)
    up()
    goto(0,0)
    down()
    right(angle)
    c=['red','blue','green']
    for count in range(12):
        name ='black'
        if(count%3==0):
           name=c[0]
        elif count%3==1:
            name=c[1]
        else:
            name=c[2]
        pencolor(name)
        forward(100)
        back(100)
        right(30)
    update()
    ontimer(draw,100)

def flick():
    state['turn']+=10

setup(420,420,370,0)
hideturtle()
width(20)
tracer(False)

onkey(lambda :flick(),'space')
listen()
up()
goto(0,0)
down()
draw()
done()




