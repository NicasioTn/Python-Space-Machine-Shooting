import pygame
import random
import math
from pygame import mixer
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, QUIT

pygame.init() # innicial = start pygame
window = pygame.display.set_mode((800, 600)) #setSize window

#set Title
pygame.display.set_caption("A Ri Ga To Game")

#set BackG
bg = pygame.image.load("D:\python\PyGame\icon\\Bg.jpg")

# Sound
#mixer.music.load('music.wav')
#mixer.music.play(-1)

#set Icon image
ico = pygame.image.load("D:\python\PyGame\icon\spiderman.png")
pygame.display.set_icon(ico)

# player
playerImg = pygame.image.load("D:\python\PyGame\icon\spidy.png")
playerX = 370
playerY = 480

p_change = 0
r_change = 0

# Enermy
enImg = pygame.image.load("D:\python\PyGame\icon\enmy.png")
#enX = 370
#enY = 40
enX = random.randint(0, 725)
enY = random.randint(40, 100)

enX_change = 0.3
enY_change = 40

# bullet
bulletImg = pygame.image.load("D:\python\PyGame\icon\shot.png")
bX = 0
bY = 480
bullet_state = "ready"
bX_change = 0
bY_change = 1

def isCollision(enX, enY, bX, bY):
    distance = math.sqrt((math.pow(enX-bX, 2))+(math.pow(enY-bY,2))) #Formula for Check Shooting
    if distance < 30 :
        return True
    else :
        return False

def player(x, y):
    window.blit(playerImg, (x, y)) #take obj on screan at x,y 

def enermy(x, y):
    window.blit(enImg, (x, y))

def shooting(x, y):
    global bullet_state # global make variable to attribute
    bullet_state = "fire"
    window.blit(bulletImg, (x+10, y+10))

score = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        #Event press key
        if event.type == pygame.KEYDOWN : #key press
            if event.key == K_LEFT : 
                p_change += -0.3
            if event.key == K_RIGHT :
                p_change += 0.3
            if event.key == K_UP :
                r_change += -0.3
            if event.key == K_DOWN :
                r_change += 0.3
            if event.key == K_SPACE and bullet_state is "ready":
                bX = playerX
                bY = playerY
                shooting(bX, bY)
                b_Sound = mixer.Sound('laser.wav')
                b_Sound.play()

        #Event Unkey press
        if event.type == pygame.KEYUP :
            if event.key == K_LEFT or event.key == K_RIGHT :
                p_change = 0
            if event.key == K_UP or event.key == K_DOWN :
                r_change = 0

    window.fill((231,35,70)) #Bg. RGB
   
    window.blit(bg,(0,0))
    
    #enX += 0.1
    enX += enX_change
    if enX >= 725:
        enX_change = -0.3
        enY += enY_change-10
    if enX <= 0:
        enX_change = 0.3
        enY += enY_change-10
    
    enermy(enX, enY)
    
    #playerX += 0.1
    playerX += p_change
    playerY += r_change
    
    # x way 
    if playerX <= 0 :
        playerX = 0
    if playerX >= 750 :
        playerX = 750
    if playerY <= 350 :
        playerY = 350
    if playerY >= 550:
        playerY = 550
    player(playerX, playerY)
    
    #Bullet Movement
    if bY <= 0:
        bY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        shooting(bX,bY)
        bY -= bY_change
    
    collision = isCollision(enX, enY, bX, bY)
    
    if collision == True :
        bullet_state = "ready"
        bY = playerY
        enX = random.randint(0,736)
        enY = random.randint(50,100)
        score += 1
        print(score)

    pygame.display.update()
    