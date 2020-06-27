import pygame
import random

#initializes pygame. Not sure if necessary anymore
#pygame.init()

#creates the screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('space.png')


#Title and Icon
pygame.display.set_caption("Space Freaks")
#For some reason, python can't open this image
'''icon = pygame.image.load('planet.png')
pygame.display.set_icon(icon)'''

#Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('ufo.png')
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyX_change = 2
enemyY_change = 40

def player(x,y):
    #blit draws
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))


running = True
while running:
    
    screen.fill((0,0,0))

    #Background image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed, check for right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change =-3
            if event.key == pygame.K_RIGHT:
                playerX_change =3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #moves enemy
    enemyX += enemyX_change

    #keeping stuff in bounds
    if enemyX >= 736:
        enemyX_change = -2
        enemyY+= enemyY_change
    elif enemyX <= 0:
        enemyX_change = 2
        enemyY+= enemyY_change
    playerX+= playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()




