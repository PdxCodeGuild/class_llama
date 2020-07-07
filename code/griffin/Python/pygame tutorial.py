import pygame
import random
import math

#initializes pygame. Not sure if necessary anymore
pygame.init()

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
enemyX = random.randint(0,735)
enemyY = random.randint(50,150)
enemyX_change = 2
enemyY_change = 40

#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = random.randint(0,736)
bulletY = 480
#ready means it's invisible
#fire means it's moving
bullet_state = "ready"
bulletX_change = 0
bulletY_change = 10

#Score
score = 0
#font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

'''def show_score(x,y):
    player_score = font.render("Score: " + str(score),True, (255,255,255))
    screen.blit(player_score,(x,y))'''

def player(x,y):
    #blit draws
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False



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
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
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

    #bullet movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change

    #collision
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score+=1
        enemyX = random.randint(0,736)
        enemyY = random.randint(50,150)

    
    player(playerX,playerY)
    #show_score(textX,textY)
    enemy(enemyX,enemyY)
    pygame.display.update()




