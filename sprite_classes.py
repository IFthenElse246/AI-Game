from math import floor
from turtle import width
import pygame
import camera_class
import global_values

#world sprite
class worldSprite:
    def __init__(this, image, isEnvironment, x=0, y=0, width = 0, height = 0, visible = True,displayPriority=1):
        this.image = image
        this.x = x
        this.y = y
        this.width = width
        this.height = height
        this.__environment = isEnvironment
        this.visible = visible
        this.displayPriority = displayPriority


        global_values.worldSprites.append(this)

    def render(this):
        width, height = this.getPixelSize()
        img = pygame.transform.scale(this.image,(width,height))
        posX, posY = this.getPixelPos()
        global_values.window.blit(img, (posX,posY))
    
    def getPixelPos(this):
        ppm = global_values.pixelsPerMeter
        wid = this.width*ppm
        heig = this.height*ppm
        x = this.x*ppm
        y = this.y*ppm

        return round(x - wid/2 - (floor(global_values.camera.x*ppm) - global_values.windowWidth/2)), round(y - heig - (floor(global_values.camera.y*ppm) - global_values.windowHeight/2))
    
    def getPixelSize(this):
        ppm = global_values.pixelsPerMeter
        wid = this.width*ppm
        heig = this.height*ppm
        return round(wid), round(heig)

    def getDisplayNumber(this):
        pr = this.displayPriority
        return this.y + pr*10000
    
    def isVisible(this):
        x,y = this.getPixelPos()
        w,h = this.getPixelSize()
        return y-h<=global_values.windowHeight and y+h>=0 and x+3*w/2>=0 and x-w/2<=global_values.windowWidth
            

    




#gui sprite