from random import *
import turtle as tt

from base import vector
from base import square


snake =[]
start = vector(0,0)
snake.append(start)
size=0
speed = vector(10,0)

def change(x,y):
    speed.x =x
    speed.y = y

def value():
    return randrange(-15,15)*10

def draw():
    global snake
    global size
    tt.clear()
    # draw food
    square(food.x,food.y,9,'green')
    # draw snake
    for piece in snake:
        print(piece.x,piece.y)
        square(piece.x,piece.y,9,'black')
    print('size ',len(snake))

def check(snake, xy):
    for p in xy:
        if(p in snake):
            return True
    return False


food = vector(value(),value())


def inside(head):
    return -200 <= head.x <= 200 and -200 <=head.y <=200

def move():
    global snake
    global size
    global food
    global speed

    dupe = snake.copy()
    snake.clear()
    for piece in dupe:
        piece.move(speed)
        if not inside(piece):
            print('Snake out of boundary')
            tt.up()
            tt.goto(0, 0)
            tt.down()
            tt.write('Your Score {}'.format(size))
            return
        snake.append(piece)
        # if check(snake):
        #     print('Snake ate itself')
        #     tt.up()
        #     tt.goto(0, 0)
        #     tt.down()
        #     tt.write('Your Score {}'.format(size))
        #     return
    if(len(snake)!=0):
        head = snake[-1]
        if(head==food):
            size+=1
            food=vector(value(),value())
            newHead=head.copy()
            newHead.move(speed)
            snake.append(newHead)
    draw()
    tt.ontimer(move,500)



tt.setup(420,420,370,0)
tt.hideturtle()
tt.tracer(False)
screen = tt.Screen()
screen.onkey(lambda: change(0,10),"Up")
screen.onkey(lambda: change(-10,0), "Left")
screen.onkey(lambda: change(0,-10), "Down")
screen.onkey(lambda: change(10,0), "Right")
screen.listen()
draw()
move()
tt.done()




