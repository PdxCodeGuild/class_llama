import pygame

#initializes pygame. Not sure if necessary anymore
#pygame.init()

#creates the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Freaks")
#For some reason, python can't open this image
'''icon = pygame.image.load('planet.png')
pygame.display.set_icon(icon)'''

#Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480

def player(x,y):
    #blit draws
    screen.blit(playerImg,(x,y))



running = True
while running:
    
    screen.fill((40,100,0))
    playerY-=.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    player(playerX,playerY)

    pygame.display.update()




