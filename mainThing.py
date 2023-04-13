import pygame
import random

#initialises pygame and creates the screen
pygame.init()
screen = pygame.display.set_mode((320, 200))
clock = pygame.time.Clock()
running = True
dt=0

#the time in between atom spawns (frames)
spawnDel=60

#image loading
playerSurface = pygame.image.load('Mr.png').convert_alpha()
tngSurface = pygame.image.load('bad_atom.png').convert_alpha()

#score
score=0

#font init
pygame.font.init()
my_font = pygame.font.Font('PixeloidMono-VGj6x.ttf', 20)


#colors
bkgYel=pygame.Color(241,252,181)

#creates the player rectangle and position vector
player_pos = pygame.Vector2(screen.get_width() / 8, screen.get_height() / 2)
plrRect=pygame.Rect(player_pos.x,player_pos.y,16,16)

#creates the enemy thing rectangle and position vector
tng_pos = pygame.Vector2(screen.get_width()-30, random.randint(0,screen.get_height()))

obstacles=[]
for _ in range(2):
    tngRect=pygame.Rect(tng_pos.x,random.randint(0,screen.get_height()),16,16)
    obstacles.append(tngRect)

#loads the sound effects
pain=pygame.mixer.Sound("hitHurt.wav")

#loads and starts the music
pygame.mixer.music.load("musical pong.mp3")
pygame.mixer.music.play(1000,0.0,1000)

while running:

    if spawnDel==0:
        tngRect=pygame.Rect(tng_pos.x,random.randint(0,screen.get_height()),16,16)
        obstacles.append(tngRect)
        tngRect=pygame.Rect(tng_pos.x,random.randint(0,screen.get_height()),16,16)
        obstacles.append(tngRect)
        spawnDel=20
    else:
        spawnDel-=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(bkgYel)

    pygame.draw.rect(screen, bkgYel, plrRect)
    screen.blit(playerSurface, plrRect)

    for tngRect in obstacles:
        if plrRect.colliderect(tngRect):
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(pain)
            pygame.time.wait(1000)
            pygame.mixer.music.play(1000,0.0,1000)
            score=0
            player_pos = pygame.Vector2(screen.get_width() / 8, screen.get_height() / 2)
            obstacles=[]
            

        tngRect[0]-=1
        if tngRect[0]==screen.get_width()/8:
            score+=1
        if tngRect[0]<-50:
            obstacles.pop(0)
        pygame.draw.rect(screen, bkgYel, tngRect)
        screen.blit(tngSurface, tngRect)

    text_surface = my_font.render(str(score), False, (0, 0, 0))

    screen.blit(my_font.render(str(score), False, (0, 0, 0)), (screen.get_width() / 2,0))

    #draws everything to the screen
    pygame.display.flip()

    #player movments
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 150 * dt
    if keys[pygame.K_s]:
        player_pos.y += 150 * dt
    if player_pos.y>screen.get_height():
        player_pos.y=1
    if player_pos.y<0:
        player_pos.y=screen.get_height()-1

    plrRect=pygame.Rect(player_pos.x,player_pos.y,16,16)

    

    dt = clock.tick(60)/1000  # limits FPS to 60 and makes dt be the time elapsed since the last frame

pygame.quit()
