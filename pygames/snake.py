import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
size_of_block =10
FPS = 15

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
gameScreen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("old snake")
clock = pygame.time.Clock()


def message_to_screen(msg,type):
    font = pygame.font.SysFont(None,25)
    screen_text = font.render(msg,True,type)
    gameScreen.blit(screen_text,[display_width/2,display_height/2])

def our_snake(snakelist,size_of_block):
    for XY in snakelist:
        pygame.draw.rect(gameScreen,green,[XY[0],XY[1],size_of_block,size_of_block])

def gameloop():
    lead_y = display_height/2
    lead_x = display_width/2

    lead_x_change =0
    lead_y_change =0
    snakelist=[]
    snakelength=1

    gameOver = False
    gameClose = False

    randAppleX = round(random.randrange(0,display_width-size_of_block)/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-size_of_block)/10.0)*10.0

    while not gameClose:


        while gameOver == True:
            gameScreen.fill(white)
            message_to_screen("To Play Again, press C, to quit press Q",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameClose = True
                    elif event.key == pygame.K_c:
                        gameloop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change =-size_of_block
                    lead_y_change =0
                elif event.key== pygame.K_RIGHT:
                    lead_x_change =size_of_block
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change =-size_of_block
                    lead_x_change = 0
                elif event.key== pygame.K_DOWN:
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
            pygame.draw.rect(gameScreen,red,(randAppleX,randAppleY,10,10))
            pygame.draw.rect(gameScreen,black,(lead_x,lead_y,10,10))
            pygame.display.update()
            snakeHead=[]
            snakeHead.append(lead_x)
            snakeHead.append(lead_y)
            if(len(snakelist)>snakelength):
                del snakelist[0]

            snakelist.append(snakeHead)

            if lead_x==randAppleX and lead_y==randAppleY:
                randAppleX = round(random.randrange(0, display_width - size_of_block) / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - size_of_block) / 10.0) * 10.0
                our_snake(snakelist, size_of_block)
            clock.tick(FPS)

    # message_to_screen("You Loose",red)
    # pygame.display.update()
    # time.sleep(2)
    pygame.quit()
    quit("HI")

gameloop()