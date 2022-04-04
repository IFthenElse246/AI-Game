import sprite_classes

class player:
    def __init__(this,image,x=0,y=0,width = 0.75,height = 1.75):
        this.sprite = sprite_classes.worldSprite(image,False,x=x,y=y,width=width,height=height)