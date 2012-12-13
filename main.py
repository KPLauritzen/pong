import pygame, sys
from pygame.locals import *

# init() should be called before anything else pygame related
pygame.init() 
# Clock object. Can make sure the fps is ~constant.
fpsClock = pygame.time.Clock()
fps = 30

(winWidth, winHeight) = (900,600)
windowSurfaceObj = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('Kaspers PONG')

blackColor = pygame.Color(0,0,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)

paddleSurfaceObj = pygame.image.load('paddle.png')

# Main loop
while True:
    # Drawing
    windowSurfaceObj.fill(blackColor)
    pygame.draw.rect(windowSurfaceObj, blueColor, (10,10, 100, 50))
    
    windowSurfaceObj.blit(paddleSurfaceObj, (100,100))
    # Making sure we can quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    fpsClock.tick(fps)

