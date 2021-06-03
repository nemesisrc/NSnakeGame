import pygame
import random
import math
from pygame import mixer
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption('nSnakeGame')
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)


size=40
n=6
blockimg = pygame.image.load('block.jpg')
blockx = [size]*n
blockx_change =0
blocky = [size]*n
blocky_change =0

appleimg = pygame.image.load('apple.png')
applex = random.randint(100, 700)
appley = random.randint(100, 550)


# background sound
mixer.music.load('bg_music_1.mp3')
mixer.music.play(-1)


def block(x, y):
    for i in range(n):
        screen.blit(blockimg, (x, y))


def apple(x, y):
    screen.blit(appleimg, (x, y))


def isCollision(blockxx, blocky, applex, appley):
    distance = math.sqrt(math.pow(blockxx[0] - applex, 2) + (math.pow(blocky[0] - appley, 2)))
    if distance < 30:
        return True
    else:
        return False


# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 30)


def show_score(x, y):
    score_value = font.render("Score : " + str(score), True, (255, 255, 255))  # boolean true means smooth edges
    screen.blit(score_value, (x, y))


# game over text
over_font = pygame.font.Font('freesansbold.ttf', 80)


def game_over_text():
    over_text = over_font.render("GAME OVER!!", True, (255, 255, 255))
    screen.blit(over_text, (130, 250))


running = True
while running:
    #screen.fill((3, 252, 169))
    # background image
    background = pygame.image.load('background.jpg')
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                blocky_change = -size
                blockx_change = 0
            elif event.key == pygame.K_DOWN:
                blocky_change = size
                blockx_change = 0
            elif event.key == pygame.K_LEFT:
                blockx_change = -size
                blocky_change = 0
            elif event.key == pygame.K_RIGHT:
                blockx_change = size
                blocky_change = 0
        # if event.type == pygame.KEYUP:
        # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
        # blockx_change=0
        # blocky_change=0

    # Collision
    collision = isCollision(blockx, blocky, applex, appley)
    if collision:
        collision_sound= mixer.Sound('1_snake_game_resources_ding.mp3')
        collision_sound.play()
        score+=1
        applex = random.randint(100, 700)
        appley = random.randint(100, 550)

    blockx[0] += blockx_change
    if blockx[0] > 800 or blockx[0] < 0:
        game_over_text()
        for i in range(n):
            blockx[i]=10000
    blocky[0] += blocky_change
    if blocky[0]> 600 or blocky[0] < 0:
        game_over_text()
        for i in range(n):
            blocky[i]=10000
    block(blockx[0],blocky[0])
    for i in range(n-1,0,-1):
        blockx[i]=blockx[i-1]
        blocky[i] = blocky[i - 1]
        block(blockx[i], blocky[i])
    time.sleep(0.15)

    apple(applex, appley)

    show_score(10,10)

    pygame.display.update()
