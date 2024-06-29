import pygame
import os
from time import sleep
from dimensiuni import *
from initialization import *
from settings import *
from superpowers import *

def move_the_line(player_pos, display, line_size, ball_pos, start_game, player_speed):
  
    display.fill("black") #reactualizeaza background-ul pentru a scapa de urmele lasate
    display.blit(player_ship, (player_pos.x-line_size/2, player_pos.y)) #afiseaza sprite-ul in centru
    pygame.draw.circle(display, "white", ball_pos, BALL_RADIUS)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        if player_pos.x + line_size/2 < DISPLAY_WIDTH:
            if start_game == False:
                ball_pos.x += player_speed     #daca nu am apasat y ca sa incepem jocul, mingea se va tine dupa bara pana ce va fi lansata
            player_pos.x += player_speed

    if keys[pygame.K_a]:
        if player_pos.x + line_size/2 > line_size:
            if start_game == False:
                ball_pos.x -= player_speed
            player_pos.x -= player_speed

def bouncing_ball(ball_pos, display, player_pos, line_size, ball_speed_x, ball_speed_y, player_speed, beep):

    ball_pos.y += ball_speed_y
    ball_pos.x += ball_speed_x
    keys = pygame.key.get_pressed()

    if ball_pos.y < 0:                    #cand mingea atinge tavanul, ricoseaza uniform
        ball_speed_y = -ball_speed_y
        beep.play()
        # ball_speed_x = (-1)* ball_speed_x
    if ball_pos.y >= player_pos.y and ball_pos.x >= player_pos.x - (line_size / 2) and ball_pos.x <= player_pos.x + (line_size / 2): #cand mingea ricoseaza din bara

        ball_speed_y = -ball_speed_y
        beep.play()
        if keys[pygame.K_a]:
            ball_speed_x += player_speed * 0.2 #simulam o forta de frecare intre minge si linie
    
        if keys[pygame.K_d]:
            ball_speed_x -= player_speed * 0.2  #simulam o forta de frecare intre minge si linie

    if ball_pos.x  <= 0 or ball_pos.x >= DISPLAY_WIDTH:
        ball_speed_x = -ball_speed_x    #cand atinge peretele drept si stang, mingea se ricoseaza uniform
        beep.play()
    return ball_speed_x, ball_speed_y

def search_block_after_coord(x, y, all_bricks):
    for block in all_bricks:
        if x == block.rect.x and y == block.rect.y:     #cautam un block dupa coordonate
            return block


def break_brick(ball_pos, all_bricks, ball_speed_x, ball_speed_y, fire_power, beep):
  
    ball_rect = pygame.Rect(ball_pos.x - BALL_RADIUS, ball_pos.y - BALL_RADIUS, 2 * BALL_RADIUS, 2 * BALL_RADIUS) #cream o forma de dreptunghi pentru minge pentru a putea detecta coliziunile

        
    for one_brick in all_bricks:
        if ball_rect.colliderect(one_brick.rect) and isinstance(one_brick, Slow)  == False and isinstance(one_brick, Fast) == False and isinstance(one_brick, MultiBalls) == False and isinstance(one_brick, FireBall) == False and isinstance(one_brick, SmallerLine) == False and isinstance(one_brick, BiggerLine) == False:
            beep.play()
            # determina partea caramizii
            brick_left = one_brick.rect.left
            brick_right = one_brick.rect.right
            brick_top = one_brick.rect.top
            brick_bottom = one_brick.rect.bottom

            # determina partea mingii
            ball_left = ball_rect.left
            ball_right = ball_rect.right
            ball_top = ball_rect.top
            ball_bottom = ball_rect.bottom

            # determina suprapunerea la fiecare coliziune
            overlap_left = ball_right - brick_left
            overlap_right = brick_right - ball_left             #calculam suprapunerile in momentul intersectiei dintre minge(ball_rect) si brick(brick_rect)
            overlap_top = ball_bottom - brick_top
            overlap_bottom = brick_bottom - ball_top

            # gaseste cea mai apropiata coliziune
            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)  #suprapunerea minima inseamna zona(laterale, deasupra, dedesubt) cea mai mare cu care mingea intersecteaza
                                                                                        #brick-ul 
            if min_overlap == overlap_left:
                # coliziune cu partea stanga a caramizii
                ball_speed_x = -ball_speed_x
                
            elif min_overlap == overlap_right:
                # coliziune cu partea dreapta a caramizii
                ball_speed_x = -ball_speed_x
             
            elif min_overlap == overlap_top:
                # coliziune cu partea de sus a caramizii
                ball_speed_y = -ball_speed_y
                
            elif min_overlap == overlap_bottom:
                # coliziune cu partea de jos a caramizii
                ball_speed_y = -ball_speed_y

            if isinstance(one_brick, GreenBrick):
                
                all_bricks = spawn_power(one_brick.rect.x, one_brick.rect.y, all_bricks)  #cand spargem o caramida verde, vom avea sansa sa spawnam o putere
                one_brick.kill()

               
            elif isinstance(one_brick, BlueBrick):

                if fire_power == False:
                    new_brick = GreenBrick(one_brick.rect.x, one_brick.rect.y, BRICK_WIDTH, BRICK_HEIGHT)
                    all_bricks.add(new_brick)
                
                one_brick.kill()

            if fire_power == True:
                explosion_sound.play()
                block1 = search_block_after_coord(one_brick.rect.x-BRICK_WIDTH, one_brick.rect.y, all_bricks)  #caramida vecina din stanga
                if block1:
                    block1.kill()
                block2 = search_block_after_coord(one_brick.rect.x, one_brick.rect.y-BRICK_HEIGHT, all_bricks)  #caramida vecina de sus
                if block2:
                    block2.kill()
                block3 = search_block_after_coord(one_brick.rect.x+BRICK_WIDTH, one_brick.rect.y, all_bricks)  #caramida vecina din dreapta
                if block3:
                    block3.kill()
                block4 = search_block_after_coord(one_brick.rect.x, one_brick.rect.y+BRICK_HEIGHT, all_bricks)  #caramida vecina de jos
                if block4:
                    block4.kill()
                block5 = search_block_after_coord(one_brick.rect.x-BRICK_WIDTH, one_brick.rect.y-BRICK_HEIGHT, all_bricks)  #caramida vecina din stanga sus
                if block5:
                    block5.kill()
                block6 = search_block_after_coord(one_brick.rect.x+BRICK_WIDTH, one_brick.rect.y-BRICK_HEIGHT, all_bricks)  #caramida vecina din dreapta sus
                if block6:
                    block6.kill()
                block7 = search_block_after_coord(one_brick.rect.x-BRICK_WIDTH, one_brick.rect.y-BRICK_HEIGHT, all_bricks)  #caramida vecina din stanga jos
                if block7:
                    block7.kill()
                block8 = search_block_after_coord(one_brick.rect.x+BRICK_WIDTH, one_brick.rect.y+BRICK_HEIGHT, all_bricks)  #caramida vecina din dreapta jos
                if block8:
                    block8.kill()
                display.blit(explosion, (ball_pos.x-100, ball_pos.y))
                
                fire_power = False #puterea functioneaza doar o singura data, apoi inceteaza
                one_brick.kill()  #cu aceasta putere, putem distruge orice tip de brick
            break  

    return ball_speed_x, ball_speed_y, fire_power


def power_motion(all_bricks, superpowers_speed):
    for block in all_bricks:
        if isinstance(block, Slow) or isinstance(block, Fast) or isinstance(block, MultiBalls) or isinstance(block, FireBall) or isinstance(block, SmallerLine) or isinstance(block, BiggerLine):
            block.rect.y += superpowers_speed 

def power_intersect_line(line_size, player_pos, all_blocks, player_speed, laser_shot, fire_power, ball_pos):
    global player_ship #pentru a putea modifica dimensiunea sprite-ului
    
    player_rect = pygame.Rect(player_pos.x - line_size/2, player_pos.y-1, line_size, 1)
    for block in all_blocks:
        if player_rect.colliderect(block):
            pick_up.play() 
            if isinstance(block, SmallerLine):
                line_size = line_size/2
                player_ship = pygame.transform.scale(player_ship_image, (int(line_size), DISPLAY_HEIGHT/50))
                block.kill()
                break
            elif isinstance(block, BiggerLine):
                if line_size < LINE_LENGTH*2:
                    line_size = line_size*2
                    player_ship = pygame.transform.scale(player_ship_image, (int(line_size), DISPLAY_HEIGHT/50))
                block.kill()
                break
            elif isinstance(block, Slow):
                if player_speed > PLAYER_SPEED/2:
                    player_speed /= 2
                block.kill()
                break
            elif isinstance(block, Fast):
                if player_speed < PLAYER_SPEED*2:
                    player_speed *= 2
                block.kill()
                break
            elif isinstance(block, MultiBalls):
                laser_shot = True
                block.kill()
                break
            elif isinstance(block, FireBall):
                fire_power = True
                block.kill()

    
    return line_size, player_speed, laser_shot, fire_power

def laser_collision_with_block(laser_rect, all_bricks, f_was_pressed):
    for block in all_bricks:
        if laser_rect.colliderect(block): 
            if isinstance(block, GreenBrick):
                
                all_bricks = spawn_power(block.rect.x, block.rect.y, all_bricks)  #cand spargem o caramida verde, vom avea sansa sa spawnam o putere
                block.kill()
                f_was_pressed = False
               
            elif isinstance(block, BlueBrick):

                new_brick = GreenBrick(block.rect.x, block.rect.y, BRICK_WIDTH, BRICK_HEIGHT)
                block.kill()
                all_bricks.add(new_brick)
                f_was_pressed = False

        if laser_rect.y <= 0:   #daca trece de background sa oprim laserele, daca nu facem asta, jocul va da crash deoarece va desena foarte multe sprite-uri
            f_was_pressed = False
       
   
    return f_was_pressed