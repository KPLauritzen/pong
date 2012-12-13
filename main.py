import pygame, sys
from pygame.locals import *
from scipy import cos, sin, random, sign

# init() should be called before anything else pygame related
pygame.init() 
# Clock object. Can make sure the fps is ~constant.
fpsClock = pygame.time.Clock()
fps = 30

(win_width, win_height) = (900,600)
windowSurfaceObj = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Kaspers PONG')

blackColor = pygame.Color(0,0,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)

leftPaddle = pygame.image.load('paddle.png')
(left_x, left_y) = (100,100)
rightPaddle = pygame.image.load('paddle.png')
(right_x, right_y) = (win_width - 100,100)


ballObj = pygame.image.load('ball.png')
(ball_x, ball_y) = (win_width/2, win_height/2)
ball_angle = random.randint(-45,45) / 180. * 3.14 # Angle in radians
ball_direction = sign(random.rand() - 0.5)
ball_speed = 5
# Compute ball x/y velocity based on angle and (magnitude of) speed 
(ball_speed_x, ball_speed_y) = (ball_direction * cos(ball_angle) * ball_speed,
                                sin(ball_angle) * ball_speed)

player_speed = 10 # in px/sec
# If a key is held down, send repeat KEYDOWN's
pygame.key.set_repeat(10, 10) 
# Main loop
while True:
    # Drawing
    windowSurfaceObj.fill(blackColor)
    windowSurfaceObj.blit(leftPaddle, (left_x, left_y))
    windowSurfaceObj.blit(rightPaddle, (right_x, right_y))
    windowSurfaceObj.blit(ballObj, (ball_x, ball_y))
    
    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    # Making sure we can quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            # movement
            elif event.key == K_DOWN:
                left_y += player_speed
            elif event.key == K_UP:
                left_y -= player_speed
    # Nothing gets drawn until this is called. 
    pygame.display.update()
    fpsClock.tick(fps)

