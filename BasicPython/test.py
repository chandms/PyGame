import turtle as tt

def wup():
    print("Up ")
    tt.down()
    tt.width(5)
    tt.color('blue')
    tt.forward(10)

def wdown():
    print("Down ")
    tt.down()
    tt.width(5)
    tt.color('red')
    tt.backward(10)

def wleft():
    print("Left ")
    tt.down()
    tt.width(5)
    tt.color('yellow')
    tt.left(45)
    tt.forward(10)

def wright():
    print("Right ")
    tt.down()
    tt.width(5)
    tt.color('green')
    tt.right(45)
    tt.forward(10)

screen = tt.Screen()
screen.onkey(wup,'Up')
screen.onkey(wdown,'Down')
screen.onkey(wleft,'Left')
screen.onkey(wright,'Right')
screen.listen()
tt.setup(420,420,370,0)
tt.hideturtle()
tt.tracer(False)
tt.done()