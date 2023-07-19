import pygame

clock = pygame.time.Clock()

pygame.init()
screen= pygame.display.set_mode((1280, 748))
pygame.display.set_caption("Pygame itProger Game")
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)



#  Player
bg = pygame.image.load('images/background.png').convert_alpha()
ghost = pygame.image.load('images/ghost.png').convert_alpha()
# ghost_x = 1300
ghost_list_in_game = []


walk_right = [
    pygame.image.load('images/player_right/right_1.png').convert_alpha(),
    pygame.image.load('images/player_right/right_2.png').convert_alpha(),
    pygame.image.load('images/player_right/right_3.png').convert_alpha(),
    pygame.image.load('images/player_right/right_4.png').convert_alpha(),
]

walk_left = [
    pygame.image.load('images/player_left/left_1.png').convert_alpha(),
    pygame.image.load('images/player_left/left_2.png').convert_alpha(),
    pygame.image.load('images/player_left/left_3.png').convert_alpha(),
    pygame.image.load('images/player_left/left_4.png').convert_alpha(),
]



player_anim_count = 0
bg_x = 0

player_speed = 10
player_x = 300
player_y = 570

is_jump = False
jump_count = 10

bg_sound = pygame.mixer.Sound('sounds/bg_music.mp3')
bg_sound.play()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 7000)

label = pygame.font.Font('fonts/VictorMono-Bold.ttf', 60)
lose_label = label.render('Вы проиграли!', False, (193, 196, 199))

gameplay = True

running = True
while running:


    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1280, 0))
    # screen.blit(ghost, (ghost_x, 570))

    if gameplay:


        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        # ghost_rest = ghost.get_rect(topleft=(ghost_x, 570))

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -10:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -10:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 2
            else:
                is_jump = False
                jump_count = 10
        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 1100:
            player_x += player_speed


        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 4
        if bg_x == -1280:
            bg_x = 0
    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (460, 290))
    # ghost_x -=10
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(1300, 570)))
    clock.tick(8)
    #  hello
