import pygame

class GameObject:
    def __init__(self,x,y,width,height,imagepath):
        image=pygame.image.load(imagepath)
        self.image=pygame.transform.scale(image,(width,height))
        self.x=x
        self.y=y
        self.width=width
        self.height=height
