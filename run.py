import pygame

resolutionDisplayWindow = (1280, 720)
windowScreen = pygame.display.set_mode(resolutionDisplayWindow)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
