from turtle import *
from random import *
from TurtleGames.base import floor,vector

tiles={}
neighbours =[
    vector(100,0),
    vector(-100,0),
    vector(0,100),
    vector(0,-100)
]

def load():
    count=1
    mark = vector(0,0)
    for y in range(-200,200,100):
        for x in range(-200,200,100):
            mark = vector(x,y)
            tiles[mark]=count
            count+=1
    tiles[mark]=None

    for count in range(50):
        neighbour = choice(neighbours)
        spot = mark + neighbour

        if spot in tiles:
            number = tiles[spot]
            tiles[spot] = None
            tiles[mark]= number
            mark = spot

def square(mark,number):
    up()
    goto(mark.x,mark.y)
    down()

    color('black', 'white')
    begin_fill()
    for c in range(4):
        forward(99)
        left(90)
    end_fill()
    
    if number is None:
        return
    elif number <10:
        forward(20)
    write(number,font=('Arial',60,'normal'))


def tap(x,y):
    x= floor(x,100)
    y = floor(y,100)

    mark = vector(x,y)
    for neighbour in neighbours:
        spot = mark + neighbour
        if spot in tiles and tiles[spot] is None:
            number = tiles[mark]
            tiles[spot] = number
            square(spot,number)
            tiles[mark]=None
            square(mark,None)


def draw():
    for mark in tiles:
        square(mark,tiles[mark])
        update()


setup(420,420,370,0)
hideturtle()
tracer(False)
load()
draw()
onscreenclick(tap)
done()


