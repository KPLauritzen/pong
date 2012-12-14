import pygame, sys
from pygame.locals import *
from scipy import cos, sin, random, sign

# init() should be called before anything else pygame related
pygame.init() 
# Clock object. Can make sure the fps is ~constant.
fpsClock = pygame.time.Clock()
fps = 30

class Box(pygame.sprite.Sprite):
    def __init__(self, color, initial_position, size):

        # All sprite classes should extend pygame.sprite.Sprite. This
        # gives you several important internal methods that you probably
        # don't need or want to write yourself. Even if you do rewrite
        # the internal methods, you should extend Sprite, so things like
        # isinstance(obj, pygame.sprite.Sprite) return true on it.
        pygame.sprite.Sprite.__init__(self)
      
        # Create the image that will be displayed and fill it with the
        # right color.
        self.image = pygame.Surface(size)
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position


(win_width, win_height) = (900,600)
windowSurfaceObj = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Kaspers PONG')

blackColor = pygame.Color(0,0,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)

leftPaddle = Box(whiteColor, (100,100), (25, 100))
rightPaddle = Box(whiteColor, (win_width - 100, 100), (25, 100))
paddles = pygame.sprite.Group(leftPaddle, rightPaddle)

upBorder = Box(blueColor, (0,0), (win_width, 15))
downBorder = Box(blueColor, (0, win_height - 15), (win_width, 15))
borders = pygame.sprite.Group(upBorder, downBorder)
# Playing with balls
(ball_x, ball_y) = (win_width/2, win_height/2)
ball = Box(whiteColor, (ball_x, ball_y), (25,25))
ball_angle = random.randint(-45,45) / 180. * 3.14 # Angle in radians
ball_direction = sign(random.rand() - 0.5)
ball_speed = 5
# Compute ball x/y velocity based on angle and (magnitude of) speed 
(ball_speed_x, ball_speed_y) = (ball_direction * cos(ball_angle) * ball_speed,
                                sin(ball_angle) * ball_speed)


player_speed = 10 # in px/sec

# controls the balls speed increase
col_count = 0
speed_multi = 1.1
# If a key is held down, send repeat KEYDOWN's
pygame.key.set_repeat(10, 10) 

# Main loop
while True:
    # Drawing
    windowSurfaceObj.fill(blackColor)
    # draw paddles
    for p in paddles:
        windowSurfaceObj.blit(p.image, p.rect)
    # draw borders
    for p in borders:
        windowSurfaceObj.blit(p.image, p.rect)
    # draw ball
    windowSurfaceObj.blit(ball.image, ball.rect)
    
    # Move ball
    ball.rect.x += ball_speed_x
    ball.rect.y += ball_speed_y
    
    # Detect collision
    if pygame.sprite.spritecollideany(ball, paddles) != None:
        ball_speed_x = -ball_speed_x
        while pygame.sprite.spritecollideany(ball, paddles) != None:
            ball.rect.x += sign(ball_speed_x) * 5
        col_count += 1
        # increase ball speed if we haven't hit max
        if col_count < 20:
            ball_speed_x *= speed_multi
            ball_speed_y *= speed_multi
    if pygame.sprite.spritecollideany(ball, borders) != None:
        ball_speed_y = -ball_speed_y
        ball.rect.y += ball_speed_y
    for p in paddles:
        colBorder = pygame.sprite.spritecollideany(p, borders)
        if colBorder != None:
            y_dist = p.rect.y - colBorder.rect.y
            if y_dist > 0: # Collision with upBorder
                p.rect.top = colBorder.rect.bottom +1
            else: # Collision with downBorder
                p.rect.bottom = colBorder.rect.top -1

    for event in pygame.event.get():
        # Making sure we can quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            # movement
            if event.key == K_DOWN:
                rightPaddle.rect.y += player_speed
            elif event.key == K_UP:
                rightPaddle.rect.y -= player_speed
            if event.key == K_s:
                leftPaddle.rect.y += player_speed
            elif event.key == K_w:
                leftPaddle.rect.y -= player_speed
    # Nothing gets drawn until this is called. 
    pygame.display.update()
    fpsClock.tick(fps)

