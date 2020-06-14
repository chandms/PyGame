from random import *
import turtle as tt
from base import vector,square

food = vector(0,0)
snake = [vector(10,0)]
aim = vector(0,-10)
score=0
FONT = ("Arial", 14, "bold")

def change(x,y):
    aim.x=x
    aim.y=y

def inside(head):
    return -200<head.x<190 and -200<head.y<190



def move():
    global score
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x,head.y,9,'red')
        tt.up()
        tt.goto(0, 0)
        tt.color('black')
        tt.down()
        tt.write('Your Score ={}'.format(score),FONT)
        tt.update()
        return
    snake.append(head)
    if head==food:
        score+=10
        print('Snake Length = ',len(snake))
        food.x = randrange(-15,15)*10
        food.y = randrange(-15,15)*10
    else:
        snake.pop(0)
    tt.clear()
    for body in snake:
        print(body.x,body.y)
        square(body.x,body.y,9,'black')
    print('--------------------------------------')
    square(food.x,food.y,9,'green')
    tt.update()
    tt.ontimer(move,1000)




tt.setup(420,420,370,0)
tt.hideturtle()
tt.tracer(False)
tt.listen()
tt.onkey(lambda :change(10,0),'Right')
tt.onkey(lambda :change(-10,0),'Left')
tt.onkey(lambda :change(0,10),'Up')
tt.onkey(lambda :change(0,-10),'Down')
move()
tt.done()







