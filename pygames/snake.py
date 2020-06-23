import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
size_of_block =20
FPS = 15

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
purple = (128,0,128)

gameScreen = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()
appleThickness = 30
snakeImage = pygame.image.load('snakehead.png')
snakeBody = pygame.image.load('snakebody.png')
appleImage = pygame.image.load('apple.png')
icon = pygame.image.load('icon.png')
direction = 'right'
pygame.display.set_caption("old snake")
pygame.display.set_icon(icon)
smallFont = pygame.font.SysFont('Comicsansms', 25)
mediumFont = pygame.font.SysFont('Comicsansms', 40)
largeFont = pygame.font.SysFont('Comicsansms', 80)

def textObjects(text,color,size):
    if size == "small":
        textSurface = smallFont.render(text,True,color)
    elif size =="medium":
        textSurface = mediumFont.render(text, True, color)
    elif size =="large":
        textSurface = largeFont.render(text, True, color)
    #font = pygame.font.SysFont(None,25)
    #textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,y_displace=0,size="small"):
    textSurface, textRect = textObjects(msg,color,size)
    textRect.center = (display_width/2),(display_height/2)+y_displace
    gameScreen.blit(textSurface,textRect)


def our_snake(snakelist,size_of_block):
    head=snakeImage
    if direction == 'right':
        head = pygame.transform.rotate(snakeImage,270)
    if direction == 'left':
        head = pygame.transform.rotate(snakeImage,90)
    if direction == 'up':
        head = snakeImage
    if direction == 'down':
        head = pygame.transform.rotate(snakeImage,180)
    gameScreen.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for XY in snakelist[:-1]:
        body = snakeBody
        if direction == 'right':
            body = pygame.transform.rotate(snakeBody,270)
        if direction == 'left':
            body = pygame.transform.rotate(snakeBody,90)
        if direction == 'up':
            body = snakeBody
        if direction == 'down':
            body = pygame.transform.rotate(snakeBody, 180)
        #pygame.draw.rect(gameScreen,green,[XY[0],XY[1],size_of_block,size_of_block])
        gameScreen.blit(body,(XY[0],XY[1]))
        pygame.display.update()
def score(score):
    text = smallFont.render("Score : {}".format(score),True,black)
    gameScreen.blit(text,[0,0])
def game_intro():
    intro = True
    while intro==True:
        gameScreen.fill(white)
        message_to_screen('Welcome',purple,-100,"large")
        message_to_screen('hope you like it',black,-30)
        message_to_screen('eat apples, you earn points',black,10)
        message_to_screen('hit yourself or the boundary, you die',black,50)
        message_to_screen('Press Space to Play or Q to Quit',black,180,"medium")
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


def gameloop():
    global direction
    lead_y = display_height/2
    lead_x = display_width/2

    lead_x_change =10
    lead_y_change =0
    snakelist=[]
    snakeHead =[]
    snakeHead.append(lead_x)
    snakeHead.append(lead_y)
    snakelist.append(snakeHead)
    snakelength=1

    gameOver = False
    gameClose = False

    randAppleX = round(random.randrange(0,display_width-size_of_block)/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-size_of_block)/10.0)*10.0

    while not gameClose:


        while gameOver == True:
            gameScreen.fill(white)
            message_to_screen("Game Over",red,-50,"large")

            message_to_screen("To Play Again, press Space, to quit press Q", black,50,"medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameClose = True
                    elif event.key == pygame.K_SPACE:
                        gameloop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change =-size_of_block
                    lead_y_change =0
                elif event.key== pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change =size_of_block
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction ='up'
                    lead_y_change =-size_of_block
                    lead_x_change = 0
                elif event.key== pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change =size_of_block
                    lead_x_change = 0
            lead_x +=lead_x_change
            lead_y +=lead_y_change
            if lead_x >=display_width or lead_x <10 or lead_y>=display_height or lead_y<0:
                message_to_screen("You Loose", red)
                pygame.display.update()
                time.sleep(2)
                gameOver = True
                continue
            gameScreen.fill(white)
            #pygame.draw.rect(gameScreen,red,(randAppleX,randAppleY,appleThickness,appleThickness))
            gameScreen.blit(appleImage,(randAppleX,randAppleY))
            our_snake(snakelist,size_of_block)
            score(snakelength-1)
            pygame.display.update()
            snakeHead=[]
            snakeHead.append(lead_x)
            snakeHead.append(lead_y)
            snakelist.append(snakeHead)
            if(len(snakelist)>snakelength):
                del snakelist[0]

            for snakebodypart in snakelist[:-1]:
                if snakebodypart == snakeHead:
                    gameOver=True

            # if lead_x==randAppleX and lead_y==randAppleY:
            #     randAppleX = round(random.randrange(0, display_width - size_of_block) / 10.0) * 10.0
            #     randAppleY = round(random.randrange(0, display_height - size_of_block) / 10.0) * 10.0
            #     snakelength+=1
            #     print(snakelist,snakelength)
            if lead_x>=randAppleX and lead_x<=randAppleX+appleThickness or lead_x + size_of_block >=randAppleX and lead_x+size_of_block<= randAppleX+appleThickness:
                if lead_y>=randAppleY and lead_y<=randAppleY+appleThickness:
                    randAppleX = round(random.randrange(0, display_width - size_of_block) / 10.0) * 10.0
                    randAppleY = round(random.randrange(0, display_height - size_of_block) / 10.0) * 10.0
                    snakelength+=1
                elif lead_y+size_of_block>=randAppleY and lead_y+size_of_block<=randAppleY+appleThickness:
                    randAppleX = round(random.randrange(0, display_width - size_of_block) / 10.0) * 10.0
                    randAppleY = round(random.randrange(0, display_height - size_of_block) / 10.0) * 10.0
                    snakelength+=1
            clock.tick(FPS)

    # message_to_screen("You Loose",red)
    # pygame.display.update()
    # time.sleep(2)
    pygame.quit()
    quit("HI")

game_intro()
gameloop()