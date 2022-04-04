from turtle import distance
import pygame
import sprite_classes
import reinforcement_learning_class
import json
import os
import time
import global_values
import camera_class
import player_class
# handles rendering and event firing

confFile = open('config.json')
conf = json.load(confFile)

maxFps = conf['maxFps']
unfocusMaxFps = conf['unfocusFps']
global_values.windowWidth = conf['startingWindowWidth']
global_values.windowHeight = conf['startingWindowHeight']
global_values.camera = camera_class.camera()
WIN = pygame.display.set_mode((global_values.windowWidth,global_values.windowHeight),pygame.RESIZABLE)
global_values.pixelsPerMeter = global_values.windowHeight/global_values.metersY
global_values.window = WIN
pygame.display.set_caption(global_values.WINDOWNAME)


plr = player_class.player(pygame.image.load(os.path.join("Assets","Player","poorlyMadePlayer.png")), width=2,height=2)
global_values.player=plr

def worldSpriteSortKey(spr):
    return spr.getDisplayNumber()

def managePlayerMovement(keys,dt):
    dirX = 0.0
    dirY = 0.0
    if keys[pygame.K_w]:
        dirY -= 1
    if keys[pygame.K_s]:
        dirY += 1
    if keys[pygame.K_a]:
        dirX -= 1
    if keys[pygame.K_d]:
        dirX += 1
    
    if not dirX == 0 or not dirY == 0:
        dist = (dirX**2 + dirY**2)**0.5
        multiplier = global_values.playerSpeed * dt
        plr.sprite.x += dirX/dist*multiplier
        plr.sprite.y += dirY/dist*multiplier


for x in range(-20,21):
    for y in range(-20,21):
        sprite_classes.worldSprite(pygame.image.load(os.path.join("Assets","Environment","poorlyMadeCrate.png")),True,x=x*2,y=y*2,width=2,height=2,displayPriority=0)

def main_loop():
    clock = pygame.time.Clock()
    running = True
    lastTime = time.time()



    while running:
        clock.tick(maxFps)
        deltaTime = time.time()-lastTime
        lastTime = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            elif event.type == pygame.VIDEORESIZE:
                global_values.windowWidth = event.w
                global_values.windowHeight = event.h
                global_values.pixelsPerMeter = event.h/global_values.metersY
        
        managePlayerMovement(pygame.key.get_pressed(),deltaTime)
        global_values.camera.smoothMove(plr.sprite.x,plr.sprite.y)
        WIN.fill((255,255,255))
        
        wSprites = global_values.worldSprites
        wSprites.sort(key=worldSpriteSortKey)
        

        for wSprite in wSprites:
            if wSprite.visible and wSprite.isVisible():
                wSprite.render()
        pygame.display.update()
    pygame.quit()
    

if __name__ == "__main__":
    main_loop()

confFile.close()