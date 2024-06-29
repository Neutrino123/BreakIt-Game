from dimensiuni import *
from initialization import *
import random

class Slow(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = slow
        self.rect = self.image.get_rect(topleft=(x,y))

class Fast(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = fast
        self.rect = self.image.get_rect(topleft=(x,y))

class MultiBalls(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = multiballs
        self.rect = self.image.get_rect(topleft=(x,y))

class FireBall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = fireball
        self.rect = self.image.get_rect(topleft=(x,y))

class SmallerLine(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = smallerline
        self.rect = self.image.get_rect(topleft=(x,y))

class BiggerLine(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = biggerline
        self.rect = self.image.get_rect(topleft=(x,y))

def spawn_power(x, y, all_bricks):
    random_number = random.randint(1, 100)   #construim sansele sa spawnam o superputere
    if random_number >= 1 and random_number <= 60:
        if random_number >= 1 and random_number <=10:
            slow_power = Slow(x, y, BRICK_WIDTH, BRICK_HEIGHT)
            all_bricks.add(slow_power)      #adaugam puterea in matricea care contine brick-urile. Cand distrugem o caramida verde vom adauga in loc o superputere care va cadea.
        if random_number >= 11 and random_number <=20:
            fast_power = Fast(x, y, BRICK_WIDTH, BRICK_HEIGHT)
            all_bricks.add(fast_power) 
        elif random_number >= 21 and random_number <=30:
            multiballs_power = MultiBalls(x, y, BRICK_WIDTH, BRICK_HEIGHT)
            all_bricks.add(multiballs_power) 
        elif random_number >= 31 and random_number <=40:
            fireball_power = FireBall(x, y, BRICK_WIDTH, BRICK_HEIGHT)
            all_bricks.add(fireball_power) 
        elif random_number >= 41 and random_number <=50:
            smallerline_power = SmallerLine(x, y, BRICK_WIDTH, BRICK_HEIGHT)
            all_bricks.add(smallerline_power) 
        elif random_number >= 51 and random_number <=60:
             biggerline_power = BiggerLine(x, y, BRICK_WIDTH, BRICK_HEIGHT)
             all_bricks.add(biggerline_power) 
        
    return all_bricks

def laser_motion(player_pos, laser_rect, laser_speed):
    
    laser_rect.y -= laser_speed
    display.blit(laser, laser_rect)

def create_laser(player_pos):

    laser_rect = pygame.Rect(player_pos.x, player_pos.y - BRICK_WIDTH , BRICK_HEIGHT-15, BRICK_WIDTH+5)
    return laser_rect
    
