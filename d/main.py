# Example file showing a basic pygame "game loop"
from typing import KeysView
import pygame
from pygame import key
from pygame import rect
from pygame.constants import BUTTON_WHEELDOWN, MOUSEBUTTONDOWN

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 400))
clock = pygame.time.Clock()
running = True
time_tick = 0
Arect = 300
a = pygame.image.load("picture\dino.png")
b = pygame.image.load("picture\cactus.png")
c = pygame.image.load("picture\Bird1.png")
a_rect = a.get_rect()
a_rect.x = 50
a_rect.y = Arect

b_rect = b.get_rect()
b = pygame.transform.scale(b,(100,100))
b_rect.x = 1200
b_rect.y = 350

c_rect = c.get_rect()
c_rect.x = 1500
c_rect.y = 250
gifspeed = 3 #3
index = 1
is_jumping = False
is_down = False
index_time = 1
g=1
jump=18
nowjump = jump
speed = 10
score = 0
gameover = False
font = pygame.font.Font(None,36)
maxscore = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                is_down = False
                Arect=300
                if not is_jumping:
                    a_rect.y = Arect
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_jumping = True
            if event.key == pygame.K_r and gameover:
                gameover = False
                score = 0  
                b_rect.x = 1200
                c_rect.x = 1500
            if event.key == pygame.K_DOWN:
                is_down = True
                Arect=330
                a_rect.y = Arect
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_jumping = True
    if is_jumping:
        a_rect.y -= nowjump
        nowjump -= g
        if a_rect.y > Arect:
            a_rect.y = Arect
            nowjump = jump
            is_jumping = False
    
    if not gameover:
        
    
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        # RENDER YOUR GAME HERE
        score_show = font.render(f"score:{score}",True,(0,0,0))
        maxscore_show = font.render(f"max score:{maxscore}",True,(0,0,0))
        gameovertext = font.render(f"game over",True,(0,0,0))
        a = pygame.image.load(f"picture\{index}.gif")
        c = pygame.image.load(f"picture\Bird{index%2}.png")
        a = pygame.transform.scale(a,(100,100))
        if is_down:
            a = pygame.transform.rotate(a, 90)
        b = pygame.transform.scale(b,(50,50))
        c = pygame.transform.scale(c,(50,50))
        index_time +=1
        if index_time == gifspeed:
            index += 1
            index_time = 0  
        screen.blit(a,a_rect)
        screen.blit(b,b_rect)
        screen.blit(c,c_rect)
        screen.blit(score_show,(10,10))
        screen.blit(maxscore_show,(10,30))
        
        
        
        if index == 14:
            index = 1
    

        b_rect.x -= speed
        if b_rect.x < -50:
            b_rect.x = 1200
            score += 1

        c_rect.x -= speed
        if c_rect.x < -50:
            c_rect.x = 1200
            score += 1

        if a_rect.colliderect(b_rect):
            if maxscore < score:
                maxscore = score
            gameover = True
        if a_rect.colliderect(c_rect):
            if maxscore < score:
                maxscore = score
            gameover = True

        if gameover:            
            maxscore_show = font.render(f"max score:{maxscore}",True,(0,0,0))
            screen.blit(gameovertext,(600,175))            
            
            
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

        
        
pygame.quit()