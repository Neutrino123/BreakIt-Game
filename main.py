# import the pygame module
import pygame
pygame.init()

from fizici import *
from initialization import *
from dimensiuni import *

#main

display, clock, player_pos, line_size, ball_pos, ball_speed_x, ball_speed_y, player_speed, laser_speed, superpowers_speed = init_game()  #initializam variabilele
all_bricks = init_level()
start_game = False
onGame = True
is_paused = False
laser_shot = True
fire_power = False
f_was_pressed = True                                                        #variabile utilizate pentru functionalitatea jocului
numar_lasere = 5
launch_game = False
aux = 0
auy = 0

while onGame:
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = False
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            onGame = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if DISPLAY_WIDTH // 3 < mouse_pos[0] < DISPLAY_WIDTH // 3 + DISPLAY_WIDTH // 3 and DISPLAY_HEIGHT // 3 < mouse_pos[1] < DISPLAY_HEIGHT // 3 + DISPLAY_HEIGHT // 10:  #suprafata butonului de start
                launch_game = True 
            elif DISPLAY_WIDTH // 3 < mouse_pos[0] < DISPLAY_WIDTH // 3 + DISPLAY_WIDTH // 3 and DISPLAY_HEIGHT // 2 < mouse_pos[1] < DISPLAY_HEIGHT // 2 + DISPLAY_HEIGHT // 10:  #suprafata butonului de quit
                onGame = False

    # Apelarea funcției meniu pentru a desena butoanele
    if launch_game == False:
        meniu(mouse_pos)    
    

    if launch_game == True:
        player_speed, ball_speed_x, ball_speed_y, superpowers_speed = change_speed(player_speed, ball_speed_x, ball_speed_y, superpowers_speed) #daca apasam tasta l vom mari miscarea, k vom micsora viteza  
        move_the_line(player_pos, display, line_size, ball_pos, start_game, player_speed)
        start_game = start_level(start_game)
        if start_game == True:
            ball_speed_x, ball_speed_y = bouncing_ball(ball_pos, display, player_pos, line_size, ball_speed_x, ball_speed_y, player_speed, beep)
    
            ball_speed_x, ball_speed_y, fire_power = break_brick(ball_pos, all_bricks, ball_speed_x, ball_speed_y, fire_power, beep)
            aux = ball_speed_x                                                                          #tinem minte vitezele. Atunci cand reluam jocul, va trebui sa reluam si vitezele de unde a ramas jocul initial
            auy = ball_speed_y
            

        player_speed, ball_speed_x, ball_speed_y, is_paused, start_game, laser_speed, superpowers_speed = pause_game(player_speed, ball_speed_x, ball_speed_y, is_paused, start_game, aux, auy, laser_speed, superpowers_speed)

        all_bricks.draw(display)                    #afiseaza atat brick-urile cat si viitoarele superputeri
        power_motion(all_bricks, superpowers_speed)                    #facem ca toate superputerile sa cada
        line_size, player_speed, laser_shot, fire_power = power_intersect_line(line_size, player_pos, all_bricks, player_speed, laser_shot, fire_power, ball_pos)   #facem modificari la viteza, lungimea barei cand bara atinge o putere
  
        if laser_shot == True:       #verificam daca am luat puterea cu lasere
        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
                f_was_pressed = True
                laser_rect = create_laser(player_pos)
                laser_sound.play()
                while f_was_pressed:       #asteptam animatia laserului. Duce la incetinirea jocului
                    laser_motion(player_pos, laser_rect, laser_speed)
                    f_was_pressed = laser_collision_with_block(laser_rect, all_bricks, f_was_pressed)  #dupa ce s-a efectuat coliziunea, f_was_pressed devine False si va iesi din while
                    pygame.display.update()
                print(numar_lasere)
                if numar_lasere == 0:
                    laser_shot = False
                    numar_lasere = 5
                numar_lasere = numar_lasere -1 #scadem numarul de lasere folosite

        if fire_power:
            pygame.draw.circle(display, "red", ball_pos, BALL_RADIUS)
    
    game_over(ball_pos, all_bricks)
    pygame.display.update()
    clock.tick(144)

#main