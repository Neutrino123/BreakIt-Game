import pygame
import os
from settings import *

display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

assets_dir = os.path.join(os.path.dirname(__file__), "assets")          #path-ul unde se afla folderul "assets"
player_ship_dir = os.path.join(assets_dir, "54-Breakout-Tiles.png")         

global player_ship_image
player_ship_image = pygame.image.load(player_ship_dir)
global player_ship                                            #incarcarea sprite-ului
player_ship = pygame.transform.scale(player_ship_image, (LINE_LENGTH, DISPLAY_HEIGHT/50))

green_brick_dir = os.path.join(assets_dir, "03-Breakout-Tiles.png")
green_brick_image = pygame.image.load(green_brick_dir)
green_brick = pygame.transform.scale(green_brick_image, (BRICK_WIDTH, BRICK_HEIGHT))

blue_brick_dir = os.path.join(assets_dir, "01-Breakout-Tiles.png")
blue_brick_image = pygame.image.load(blue_brick_dir)
blue_brick = pygame.transform.scale(blue_brick_image, (BRICK_WIDTH, BRICK_HEIGHT))

gray_brick_dir = os.path.join(assets_dir, "17-Breakout-Tiles.png")
gray_brick_image = pygame.image.load(gray_brick_dir)
gray_brick = pygame.transform.scale(gray_brick_image, (BRICK_WIDTH, BRICK_HEIGHT))

heart_dir = os.path.join(assets_dir, "60-Breakout-Tiles.png")
heart_image = pygame.image.load(heart_dir)
heart = pygame.transform.scale(heart_image, (BRICK_WIDTH, BRICK_HEIGHT))

slow_dir = os.path.join(assets_dir, "41-Breakout-Tiles.png")
slow_image = pygame.image.load(slow_dir)
slow = pygame.transform.scale(slow_image, (BRICK_WIDTH, BRICK_HEIGHT))

fast_dir = os.path.join(assets_dir, "42-Breakout-Tiles.png")
fast_image = pygame.image.load(fast_dir)
fast = pygame.transform.scale(fast_image, (BRICK_WIDTH, BRICK_HEIGHT))

multiballs_dir = os.path.join(assets_dir, "43-Breakout-Tiles.png")
multiballs_image = pygame.image.load(multiballs_dir)
multiballs = pygame.transform.scale(multiballs_image, (BRICK_WIDTH, BRICK_HEIGHT))

fireball_dir = os.path.join(assets_dir, "44-Breakout-Tiles.png")
fireball_image = pygame.image.load(fireball_dir)
fireball = pygame.transform.scale(fireball_image, (BRICK_WIDTH, BRICK_HEIGHT))

smallerline_dir = os.path.join(assets_dir, "46-Breakout-Tiles.png")
smallerline_image = pygame.image.load(smallerline_dir)
smallerline = pygame.transform.scale(smallerline_image, (BRICK_WIDTH, BRICK_HEIGHT))

biggerline_dir = os.path.join(assets_dir, "47-Breakout-Tiles.png")
biggerline_image = pygame.image.load(biggerline_dir)
biggerline = pygame.transform.scale(biggerline_image, (BRICK_WIDTH, BRICK_HEIGHT))

laser_dir = os.path.join(assets_dir, "61-Breakout-Tiles.png")
laser_image = pygame.image.load(laser_dir)
laser = pygame.transform.scale(laser_image, (BRICK_HEIGHT-15, BRICK_WIDTH-20))

start_game_button_dir = os.path.join(assets_dir, "Untitled.png")
start_game_button_image = pygame.image.load(start_game_button_dir)
start_game_button = pygame.transform.scale(start_game_button_image, (DISPLAY_WIDTH/3, DISPLAY_HEIGHT/5))

start_game_hover_button_dir = os.path.join(assets_dir, "startgame_hover.png")
start_game_hover_button_image = pygame.image.load(start_game_hover_button_dir)
start_game_hover_button = pygame.transform.scale(start_game_hover_button_image, (DISPLAY_WIDTH/3, DISPLAY_HEIGHT/5))

beep_dir = os.path.join(assets_dir, 'one_beep.mp3')
beep = pygame.mixer.Sound(beep_dir)

pick_up_dir = os.path.join(assets_dir, 'pick_up.mp3')
pick_up = pygame.mixer.Sound(pick_up_dir)

laser_sound_dir = os.path.join(assets_dir, 'laser.mp3')
laser_sound = pygame.mixer.Sound(laser_sound_dir)

explosion_dir = os.path.join(assets_dir, 'explosion.mp3')
explosion_sound = pygame.mixer.Sound(explosion_dir)

explosion_image_dir = os.path.join(assets_dir, "explozie.png")
explosion_image = pygame.image.load(explosion_image_dir)
explosion = pygame.transform.scale(explosion_image, (BRICK_WIDTH*3, BRICK_HEIGHT*3))




