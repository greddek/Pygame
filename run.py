# Author: LJ
# Description:  Simple game for learning Python rules and clear code rules
#               Comments are just for study

import pygame, sys

# initialization for modules ex. clock
pygame.init()
resolutionWindow    = (1280, 720)
deltaTime           = 0.0
convertForSeconds   = 1000.0
maxTimePerSecond    = 70.0
NormalizationTime   = 1 / maxTimePerSecond
boxObject           = pygame.Rect(10, 50, 200, 100)
windowScreen        = pygame.display.set_mode(resolutionWindow)
# object clock tick for delay
clockDelay = pygame.time.Clock()


while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
    # Ticking normalization for standard move on all processors
    deltaTime += (clockDelay.tick() / convertForSeconds)
    while deltaTime > NormalizationTime:
        deltaTime -= NormalizationTime
        # Steering of the object
        if pygame.key.get_pressed()[pygame.K_d]:
            boxObject.x += 1
        elif pygame.key.get_pressed()[pygame.K_s]:
            boxObject.y += 1
        elif pygame.key.get_pressed()[pygame.K_w]:
            boxObject.y -= 1
        elif pygame.key.get_pressed()[pygame.K_a]:
            boxObject.x -= 1

    # Refresh and draw new object
    windowScreen.fill((0, 0, 0))
    pygame.draw.rect(windowScreen, (0, 150, 255), boxObject)
    pygame.display.flip()
