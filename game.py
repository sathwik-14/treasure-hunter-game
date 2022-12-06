import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy
class Game:
    def __init__(self):
        self.width=800
        self.height=800
        self.white_color=(255,255,255)

        self.screen=pygame.display.set_mode((self.width,self.height))
        self.clock=pygame.time.Clock()
        back_in=pygame.image.load('assets/background.png')
        tres_in=pygame.image.load('assets/treasure.png')
        g0_in=pygame.image.load('assets/go.png')
        self.g0=GameObject(0,0,800,800,'assets/go.png')
        self.background=GameObject(0,0,800,800,'assets/background.png')
        self.treasure=GameObject(375,80,50,50,'assets/treasure.png')
        
        self.level=1.0
        self.reset_map()

    def reset_map(self):
            self.player=Player(375,725,50,50,'assets/player.png',10)
            
            speed=5+(self.level * 5)

            if self.level>=5.0:
                 self.enemies=[
                    Enemy(50,600,50,50,'assets/enemy.png',speed),
                    Enemy(750,400,50,50,'assets/enemy.png',speed),
                    Enemy(50,200,50,50,'assets/enemy.png',speed) ]   
            elif self.level>=3.0:
                self.enemies=[
                    Enemy(50,600,50,50,'assets/enemy.png',speed),  
                    Enemy(750,400,50,50,'assets/enemy.png',speed) ]
            else:
                self.enemies=[Enemy(50,600,50,50,'assets/enemy.png',speed)]
        
       

    def move_objects(self,player_direction):
        self.player.move(player_direction,self.height,700)
        for enemy in self.enemies:
            enemy.move(self.width)

    def detect_collision(self,obj1,obj2):      
        if obj1.y>obj2.y+obj2.height:
                    return False
        elif obj2.y>obj1.y+obj1.height:
                    return False
                    
        if obj1.x>obj2.x+obj2.width:
                    return False
        elif obj2.x>obj1.x+obj1.width:
                    return False
        return True 

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player,enemy):
                self.level=1.0
                return self.reset_map()
        if self.detect_collision(self.player,self.treasure):
            
            self.level+=1.0
            return self.reset_map() 
        return False


    def draw_objects(self):
        self.screen.fill(self.white_color)
        self.screen.blit(self.background.image,(self.background.x,self.background.y))
        self.screen.blit(self.treasure.image,(self.treasure.x,self.treasure.y))
        self.screen.blit(self.player.image,(self.player.x,self.player.y))
        for enemy in self.enemies:
            self.screen.blit(enemy.image,(enemy.x,enemy.y))
        if self.level>5:
            self.screen.blit(self.g0.image,(self.g0.x,self.g0.y))
            
        pygame.display.update()


    def run_game_loop(self):
        player_direction=0;
        while True:
            events=pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction=-1
                    if event.key == pygame.K_DOWN:
                        player_direction=1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction=0

            self.move_objects(player_direction)

          

            self.draw_objects()

            if self.check_if_collided():
                return self.reset_map()

            self.clock.tick(60)
