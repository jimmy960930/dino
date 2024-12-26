# Example file showing a basic pygame "game loop"
from typing import KeysView
import pygame
from pygame import key
from pygame import rect
from pygame.constants import BUTTON_WHEELDOWN, MOUSEBUTTONDOWN
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 400))
clock = pygame.time.Clock()
running = True
time_tick = 0
Arect = 300
a = pygame.image.load(r"picture\dino.png")
b = pygame.image.load(r"picture\cactus.png")
c = pygame.image.load(r"picture\Bird1.png")
track = pygame.image.load(r"picture\Track.png")
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

track_rect = track.get_rect()
track_rect.x=0
track_rect.y=350
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
    for event in pygame.event.get():  #按鍵偵測
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                is_down = False
                Arect=a_rect.y-30
                a_rect.y = Arect
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_jumping = True
            if event.key == pygame.K_r and gameover:
                gameover = False
                score = 0  
                b_rect.x = 1280
                c_rect.x = 2000
                speed = 10
            if event.key == pygame.K_DOWN:
                is_down = True
                Arect=a_rect.y+30
                a_rect.y = Arect
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_jumping = True
    if is_jumping:
        a_rect.y -= nowjump
        nowjump -= g
        if a_rect.y > (300,330)[is_down]:
            a_rect.y = (300,330)[is_down]
            nowjump = jump
            is_jumping = False
    
    if not gameover:  #主程式碼
        
        
        screen.fill("white")
        screen.blit(track,track_rect)
        
        score_show = font.render(f"score:{score}",True,(0,0,0))
        maxscore_show = font.render(f"max score:{maxscore}",True,(0,0,0))
        gameovertext = font.render(f"game over",True,(0,0,0))
        speed_show = font.render(f"speed:{speed}",True,(0,0,0))
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
        screen.blit(speed_show,(1100,10))
        
        
        
        if index == 14:
            index = 1
    

        b_rect.x -= speed
        if b_rect.x < -50:
            b_rect.x = random.randint(1280,2000)
            score += 1
            if score % 3 == 0:
                speed+=1
        
        c_rect.x -= speed
        if c_rect.x < -50:
            c_rect.x = random.randint(1280,2000)
            score += 1
            if score % 3 == 0:
                speed+=1
        track_rect.x -= speed
        if track_rect.x < -200:
            track_rect.x = 0
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
            
            
        pygame.display.flip()

        clock.tick(60)  

        
        
pygame.quit()