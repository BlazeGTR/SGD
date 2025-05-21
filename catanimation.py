import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
s_catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
s_catx = 15
s_caty = 10
direction = 'right'
s_direction = 'left'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    if s_direction == 'right':
        s_catx += 5
        if s_catx == 280:
            s_direction = 'up'
    elif s_direction == 'down':
        s_caty += 5
        if s_caty == 220:
            s_direction = 'right'
    elif s_direction == 'left':
        s_catx -= 5
        if s_catx == 10:
            s_direction = 'down'
    elif s_direction == 'up':
        s_caty -= 5
        if s_caty == 10:
            s_direction = 'left'

    DISPLAYSURF.blit(catImg, (catx, caty))
    DISPLAYSURF.blit(s_catImg, (s_catx, s_caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
