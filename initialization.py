import pygame
import os
from dimensiuni import *
from settings import *
import random


class GreenBrick(pygame.sprite.Sprite):                     #clasa ce mosteneste clasa pygame.sprite.Sprite, ne ajuta sa utilizam cat mai usor sprite-urile
    def __init__(self, x, y, width, height):   
        super().__init__()
        self.image = green_brick
        self.rect = self.image.get_rect(topleft=(x, y))

class BlueBrick(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):   
        super().__init__()
        self.image = blue_brick
        self.rect = self.image.get_rect(topleft=(x, y))

class GrayBrick(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):   
        super().__init__()
        self.image = gray_brick
        self.rect = self.image.get_rect(topleft=(x, y))

# Funcția pentru desenarea unui buton
def draw_button(text, x, y, width, height, color, hover_color, mouse_pos):
    if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
        pygame.draw.rect(display, hover_color, (x, y, width, height))             #cand dam cu mouse-ul pe buton, isi schimba butonul culoarea
    else:
        pygame.draw.rect(display, color, (x, y, width, height))                      
    font = pygame.font.Font(None, 36)

    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))   
    display.blit(text_surf, text_rect)      #afisam textul pe butoane

def meniu(mouse_pos):
    display.fill(WHITE)
    
    # Desenarea butoanelor
    draw_button("Start Game", DISPLAY_WIDTH // 3, DISPLAY_HEIGHT // 3, DISPLAY_WIDTH // 3, DISPLAY_HEIGHT // 10, GREY, LIGHT_GREY, mouse_pos)
    draw_button("Quit", DISPLAY_WIDTH // 3, DISPLAY_HEIGHT // 2, DISPLAY_WIDTH // 3, DISPLAY_HEIGHT // 10, GREY, LIGHT_GREY, mouse_pos)


def init_game():
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()
    line_size = LINE_LENGTH
    player_pos = pygame.Vector2(DISPLAY_WIDTH/2, DISPLAY_HEIGHT / 1.1)                          #initializam variabile importante pentru functionalitatea jocului, variabile ce
    ball_pos =  pygame.Vector2(player_pos.x, player_pos.y +2)                                 #se vor schimba pe parcursul jocului
    ball_speed_y = BALL_SPEED_Y
    ball_speed_x = BALL_SPEED_X
    player_speed = PLAYER_SPEED
    laser_speed = LASER_SPEED
    superpowers_speed = SUPERPOWERS_SPEED
    return display, clock, player_pos, line_size, ball_pos, ball_speed_x, ball_speed_y, player_speed, laser_speed, superpowers_speed

def start_level(start_game):

    keys = pygame.key.get_pressed()
    if keys[pygame.K_y]:
        start_game = True           #se activeaza atunci cand lansam mingea
    return start_game

def change_speed(player_speed, ball_speed_x, ball_speed_y, superpowers_speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_l]:
        player_speed *= 1.1
        ball_speed_x *= 1.1
        ball_speed_y *= 1.1
        superpowers_speed *= 1.1
    if keys[pygame.K_k]:
        player_speed /= 1.1
        ball_speed_x /= 1.1
        ball_speed_y /= 1.1
        superpowers_speed /= 1.1

    return player_speed, ball_speed_x, ball_speed_y, superpowers_speed

def init_level():
    all_bricks = pygame.sprite.Group()
    
    for i in range(0, int(DISPLAY_HEIGHT / 3), BRICK_HEIGHT):
        for j in range(0, DISPLAY_WIDTH, BRICK_WIDTH+50):

            random_number = random.randint(1, 10)               #fiecare brick il punem random(gri, albastru sau verde)

            if random_number == 1 or random_number == 2 or random_number == 3:
                brick = GreenBrick(j, i, BRICK_WIDTH, BRICK_HEIGHT)
            elif random_number == 4 or random_number == 5 or random_number == 6 or random_number == 7 or random_number == 8:
                brick = BlueBrick(j, i, BRICK_WIDTH, BRICK_HEIGHT)
            else:
                brick = GrayBrick(j, i, BRICK_WIDTH, BRICK_HEIGHT)

            all_bricks.add(brick)

    return all_bricks

def pause_game(player_speed, ball_speed_x, ball_speed_y, is_paused, start_game, aux, auy, laser_speed, superpowers_speed):
   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
            
        is_paused = not is_paused #mereu cand apasam SPACE, variabila is_paused devine True sau False
    
        if is_paused == True:
            pygame.time.wait(100)
            start_game = False
            player_speed = 0
            ball_speed_x = 0
            ball_speed_y = 0
            laser_speed = 0
            superpowers_speed = 0
            
            
        else:
            pygame.time.wait(100)
            start_game = True
            player_speed = PLAYER_SPEED
            ball_speed_y = auy
            ball_speed_x = aux
            laser_speed = LASER_SPEED
            superpowers_speed = SUPERPOWERS_SPEED
          
            

    return player_speed, ball_speed_x, ball_speed_y, is_paused, start_game, laser_speed, superpowers_speed


def game_over_screen(message):
    display.fill(BLACK)
    large_font = pygame.font.Font(None, 72)
    text_surf = large_font.render(message, True, WHITE)
    text_rect = text_surf.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2))   #scriem mesajul "You Lost pe fundal"
    display.blit(text_surf, text_rect)
    pygame.display.update()
    pygame.time.wait(3000)  # Așteaptă 3 secunde

def game_over(ball_pos, all_bricks):
    if ball_pos.y >= DISPLAY_HEIGHT:
        game_over_screen("You Lost")
      # Indică faptul că jocul s-a terminat

    ai_castigat = True
    for block in all_bricks:
        if isinstance(block, GreenBrick) or isinstance(block, BlueBrick):    #verificam de fiecare data daca mai avem vreun brick verde sau albastru, daca niciunul nu mai e, am castigat
            ai_castigat = False
            break

    if ai_castigat:
        game_over_screen("You Won")
    

