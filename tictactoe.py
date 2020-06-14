from turtle import *
from base import line

FONT = ("Arial", 16, "bold")
taken=[

    [-200.0,66.0],[-67.0,66.0],[66.0,66.0],
    [-200.0,-67.0],[-67.0,-67.0],[66.0,-67.0],
    [-200.0,-200.0],[-67.0,-200.0],[66.0,-200.0]
]

step = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}

def grid():
    line(-67,200,-67,-200)
    line(67, 200, 67, -200)
    line(-200,-67,200,-67)
    line(-200, 67, 200, 67)

def drawx(x,y):
    pencolor('blue')
    width('4')
    line(x,y,x+133,y+133)
    line(x,y+133,x+133,y)

def drawo(x,y):
    up()
    goto(x+67,y+5)
    down()
    pencolor('red')
    width('3')
    circle(62)

def floor(value):
    return ((value+200)//133)*133 -200

state  ={'player' : 0}
players = [drawx,drawo]

def check(x,y,player):
    ll=[x,y]
    if ll in taken:
        ind = taken.index(ll)
        if step[ind]==0:
            if(player==0):
                step[ind]=1
            else:
                step[ind]=2
            return True
        else:
            return False
    return False

def win(player):
    global taken
    myPlayer = player + 1
    if step[0]==step[1]==step[2]==myPlayer:
        return True
    if step[0]==step[3]==step[6]==myPlayer:
        return True
    if step[6]==step[7]== step[8] == myPlayer:
        return True
    if step[2]== step[5]==step[8]==myPlayer:
        return True
    if step[1]==step[4]== step[7]==myPlayer:
        return True
    if step[3]== step[4]==step[5]==myPlayer:
        return True
    if step[0]== step[4]==step[8]==myPlayer:
        return True
    if step[2]== step[4]== step[6]==myPlayer:
        return True


def tap(x,y):
    x = floor(x)
    y = floor(y)
    player = state['player']
    if check(x,y,player) == False:
        return

    draw = players[player]
    draw(x,y)
    if(win(player)==True):
        up()
        goto(0,0)
        down()
        write('player {} wins'.format(player+1),font=FONT)
        update()
        return
    update()
    state['player'] = not player


setup(410,410,370,0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
