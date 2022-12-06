import pygame
from gameObject import GameObject
class Player(GameObject):
    def __init__(self,x,y,width,height,imagepath,speed):
        super().__init__(x,y,width,height,imagepath)
        self.speed=speed

    def move(self,direction,max_height,max_down):
        
            if (self.y>=max_height-self.height) or self.y==0:
                if direction<0 :
                    return
                else:
                    self.y+=(direction * self.speed)
            elif self.y>=max_down:
                if direction>0:
                    return
                else:
                    self.y+=(direction * self.speed)
            self.y+=(direction * self.speed)
        