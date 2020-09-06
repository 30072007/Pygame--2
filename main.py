import pygame

#initailazation
pygame.init()

#display here, >>((800, 600))<< you can tell your height and length in pixels
screen = pygame.display.set_mode((800, 600))

#Text and icon
pygame.display.set_caption("name of your window")
icon = pygame.image.load('joystick.png')
pygame.display.set_icon(icon)

#last time we added this (up there)
#now this

#game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #screen.fill ((R, G, B)) (Red, Green, Blue)
    screen.fill ((255, 0, 0))
    pygame.display.update()