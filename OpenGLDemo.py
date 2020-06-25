from OpenGL import *
import pygame

from pygame.locals import  *

from OpenGL.GL import *

from OpenGL.GLU import *

vertices =(

    (0,0,0),
    (1,0,0),
    (1,1,0),
    (0,1,0),
    (0,1,1),
    (1,0,1),
    (0,0,1),
    (1,1,1)
)

edges=(


    (0,1),(0,3),(0,6),(1,2),(1,5),(2,3),
    (2,7),(3,4),(4,7),(4,6),(5,6),(5,7)
)


def draw():
    glBegin(GL_LINE)

    for edge in edges:
        for node in edge:
            glVertex3fv(vertices[node])
    glEnd()

def main():
    pygame.init()
    display = (800,600)

    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    gluPerspective(45.0,(display[0]/display[1]),1,50.0)
    glTranslatef(0.0,0.0,-5.0)
    glRotatef(18,0,0,0)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_COLOR_BUFFER_BIT)
        draw()
        pygame.display.update()
        pygame.time.wait(10)


main()

