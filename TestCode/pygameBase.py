import pygame, sys, time

from pygame.locals import *

import ./Collisions

# set up pygame

pygame.init()

 

# set up the window

WINDOWWIDTH = 400

WINDOWHEIGHT = 400

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

pygame.display.set_caption('Animation')

BallCount = 9

BallCoords = [(100,100),(200,100),(300,100),(100,200),(200,200),(300,200),(100,300),(200,300),(300,300),]

t = table([(0,0),(WINDOWWIDTH,WINDOWHEIGHT)],0,0)

for i in range(BallCount-1):
    t.addBall(ball(1,1,10,BallCoords[i]))
    
t._ballArr[0]._vector._magnitude = 5
t._ballArr[0]._vector._direction = 0.6

BLUE = (0, 0, 255)


resultCoords = []
currTime = 0
# run the game loop

while True:

    # check for the QUIT event

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()



    # draw the black background onto the surface

    windowSurface.fill(BLACK)


    resultCoords = table().tableStateSnapshot(currTime)
    for r in resultCoords:

        


       # draw the block onto the surface
        pygame.draw.circle(windowSurface, BLUE, r, 40)



    # draw the window onto the screen

    pygame.display.update()

    time.sleep(0.02)
    currTime += 1