import random
import pygame
import Enemy
import NateHunter
import time

pygame.mixer.init()

pygame.mixer.music.load("Sounds/scaryMusic2.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
gunshot_channel = pygame.mixer.Channel(1)
gunshot_sound = pygame.mixer.Sound("Sounds/shoot_shotgun.wav")
gunshot_sound.set_volume(0.1)
pickUp_channel = pygame.mixer.Channel(3)
pickUp_sound = pygame.mixer.Sound("Sounds/PickUp.wav")
pickUp_sound.set_volume(0.03)
death_chanel = pygame.mixer.Channel(4)
death_sound = pygame.mixer.Sound("Sounds/loss.wav")
death_sound.set_volume(.1)
reload_channel = pygame.mixer.Channel(2)
reload_sound = pygame.mixer.Sound("Sounds/reload.wav")
reload_sound.set_volume(0.2)

normal_img = pygame.image.load('images/zombie.png')
normal_img = pygame.transform.scale(normal_img, (125, 125))

tank_img = pygame.image.load('images/tank.png')
tank_img = pygame.transform.scale(tank_img, (125, 125))

normal_nate = pygame.image.load('images/Nate.png')
normal_nate_img = pygame.transform.scale(normal_nate, (125, 125))

nate_tank = pygame.image.load('images/HeavyNate.png')
nate_tank_img = pygame.transform.scale(nate_tank, (125, 125))

shotgun_img = pygame.transform.scale(pygame.image.load('images/shotgun.png'), (100, 75))
shotgun_sprite = pygame.sprite.Sprite()
shotgun_sprite.image = shotgun_img
shotgun_sprite.rect = shotgun_sprite.image.get_rect()

pistol_img = pygame.transform.scale(pygame.image.load('images/pistol.png'), (65, 65))
pistol_img = pygame.transform.flip(pistol_img, True, False)
pistol_sprite = pygame.sprite.Sprite()
pistol_sprite.image = pistol_img
pistol_sprite.rect = pistol_sprite.image.get_rect()

healthpack_img = pygame.transform.scale(pygame.image.load('images/healthpack.png'), (50, 50))
healthpack_sprite = pygame.sprite.Sprite()
healthpack_sprite.image = healthpack_img
healthpack_sprite.rect = healthpack_sprite.image.get_rect()

armour_img = pygame.transform.scale(pygame.image.load('images/armor.png'), (49, 49))
armour_sprite = pygame.sprite.Sprite()
armour_sprite.image = armour_img
armour_sprite.rect = armour_sprite.image.get_rect()

flash_img = pygame.image.load('images/fire.png')
flash_img = pygame.transform.scale(flash_img, (40, 40))
flash_sprite = pygame.sprite.Sprite()
flash_sprite.image = flash_img
flash_sprite.rect = flash_sprite.image.get_rect()

tank = (50, 1, 1, "tank", tank_img)  # health, speed, damage, type, img
normal = (30, 2, 1, "normal", normal_img)  # health, speed, damage, type, img

enemies_killed = 0
loot_picked_up = False
next_lvl = False

zombie_count = 0
bullets = 7
death_sound_played = False

def create_zombie(numNormal, numTank, player):
    count = 0
    zombie_group = pygame.sprite.Group()
    zombie_group2 = pygame.sprite.Group()
    while count < numNormal:
        x = random.randint(0, 800)
        y = random.randint(150, 800)
        zombie = Enemy.Enemy(x, y, player, normal[0], normal[1], normal[2], normal[3], normal[4])
        zombie_group.add(zombie)
        count += 1
    count = 0
    while count < numTank:
        x = random.randint(0, 800)
        y = random.randint(150, 800)
        zombie = Enemy.Enemy(x, y, player, tank[0], tank[1], tank[2], tank[3], tank[4])
        zombie_group.add(zombie)
        count += 1

    return zombie_group


pygame.init()
cursor_img = pygame.image.load('images/cursor.png')
cursor_img = pygame.transform.scale(cursor_img, (50, 50))

pygame.mouse.set_visible(False)
cursor_img_rect = cursor_img.get_rect()

dead = False

restart_img = pygame.transform.scale(pygame.image.load('images/restart.png'), (250, 200))
restart_sprite = pygame.sprite.Sprite()
restart_sprite.image = restart_img
restart_sprite.rect = restart_sprite.image.get_rect()

next_lvl_img = pygame.transform.scale(pygame.image.load('images/nextlevel.png'), (250, 100))
next_lvl_sprite = pygame.sprite.Sprite()
next_lvl_sprite.image = next_lvl_img
next_lvl_sprite.rect = next_lvl_sprite.image.get_rect()

bg_image = pygame.image.load('images/level.png')

bg_image = pygame.transform.scale(bg_image, (800, 800))
bg_rect = bg_image.get_rect()

health_img = pygame.image.load('images/heart3.png')
health_img = pygame.transform.scale(health_img, (75, 25))
health_rect = health_img.get_rect()

screen = pygame.display.set_mode((bg_rect.width, bg_rect.height))
screen_rect = screen.get_rect()

pygame.display.set_caption("Nate Hunter: Pixel Apocalypse")

# Load and set the game logo/icon
logo = pygame.image.load('images/natelogo.png')  # Replace "logo.png" with the path to your logo image
pygame.display.set_icon(logo)

player_group = pygame.sprite.Group()
barrier_group = pygame.sprite.Group()
button_group = pygame.sprite.Group()
loot_group = pygame.sprite.Group()
loot_group.add(shotgun_sprite)
loot_group.add(healthpack_sprite)
loot_group.add(armour_sprite)
for sprite in loot_group:
    sprite.rect.center = (random.randint(1, 600), random.randint(300, 600))

pos = (400, 400)
NateHunter.Player(screen, pos, player_group, barrier_group, 90)

enemy_group = create_zombie(3, 2, player_group.sprites()[0])
zombie_count = 5
flash_group = pygame.sprite.Group()
start_time = 0
reload = False

clock = pygame.time.Clock()
last_click_time = 0
flash_timer = 0
zombies_killed = 0
spawn_timer = 0
reload = False
bullets = 7
bullet_timer1 = 0
has_shotgun = False
timer = False
words = ""
did_reload = False
weapon = "pistol"
def reset():
    global next_lvl, current_level, level_complete, game_over, bg_image, bg_rect, enemies_killed, bullets, next_lvl, zombie_count, dead, start_time, reload, time_elapsed, has_shotgun, weapon, death_sound_played

    # Reset player
    player_group.sprites()[0].health = 100
    player_group.sprites()[0].rect.x = 400
    player_group.sprites()[0].rect.y = 400
    weapon = "pistol"
    player_group.sprites()[0].gun_image = pistol_img
    player_group.sprites()[0].image = normal_nate
    player_group.sprites()[0].image_path = 'images/Nate.png'
    player_group.sprites()[0].health = 90
    player_group.sprites()[0].max_health = 90
    has_shotgun = False
    death_sound_played = False

    # Reset enemies
    enemy_group.empty()
    enemy_group.add(create_zombie(3, 2, player_group.sprites()[0]))

    # Reset loot
    loot_group.empty()
    loot_group.add(shotgun_sprite)
    loot_group.add(healthpack_sprite)
    loot_group.add(armour_sprite)
    for sprite in loot_group:
        sprite.rect.center = (random.randint(1, 600), random.randint(300, 600))

    # Reset game state variables
    current_level = 1
    level_complete = False
    game_over = False
    enemies_killed = 0
    bullets = 7
    next_lvl = False
    zombie_count = 5
    dead = False
    start_time = pygame.time.get_ticks()

    bg_image = pygame.image.load('images/level.png')

    # Reset background image
    bg_image = pygame.image.load('images/level.png')
    bg_image = pygame.transform.scale(bg_image, (800, 800))
    bg_rect = bg_image.get_rect()

    # Update screen
    screen.blit(bg_image, (0, 0))
    pygame.display.flip()

    # Reset background image
    bg_image = pygame.image.load('images/level.png')
    bg_image = pygame.transform.scale(bg_image, (800, 800))
    bg_rect = bg_image.get_rect()

    # Update screen
    screen.blit(bg_image, (0, 0))
    pygame.display.flip()


def draw_timer(start_time, x, y):
    time_elapsed = (pygame.time.get_ticks() - start_time) / 1000
    font = pygame.font.Font('Fonts/Minecraft.ttf', 25)
    minutes = int(time_elapsed // 60)
    seconds = int(time_elapsed % 60)
    time_format = f"{minutes:02}:{seconds:02}"
    text = font.render(time_format, False, (255, 255, 255))
    screen.blit(text, (x, y))
    return time_format


time_elapsed = 0


def render():
    num_bg_images_x = (screen_rect.width // bg_rect.width) + 2
    num_bg_images_y = (screen_rect.height // bg_rect.height) + 2

    # Blit the background image multiple times with a horizontal offset based on the player's x position
    for i in range(num_bg_images_x):
        for j in range(num_bg_images_y):
            # Calculate the offsets for x and y direction scrolling
            bg_offset_x = bg_rect.width * i - player_group.sprites()[0].rect.x % bg_rect.width
            screen.blit(bg_image, (bg_offset_x, 0))

    # Draw the player and update the display
    player_group.update()
    player_group.draw(screen)

    enemy_group.update()
    enemy_group.draw(screen)

    flash_group.draw(screen)

    loot_group.update()
    loot_group.draw(screen)

    button_group.update()
    button_group.draw(screen)

    # enemy_group3.update()
    # enemy_group3.draw(screen)

    screen.blit(health_img, (5, 5))

    if timer:
        global words
        words= draw_timer(start_time, 700, 10)


    cursor_img_rect.center = pygame.mouse.get_pos()  # update position
    screen.blit(cursor_img, cursor_img_rect)  # draw the cursor

    font = pygame.font.Font('Fonts/Minecraft.ttf', 25)

    if (reload == True):
        text1 = font.render("Reloading", True, (255, 255, 255))
    elif (bullets < 0):
        text1 = font.render("Bullets Remaining: " + str(bullets + 1), True, (255, 255, 255))
    else:
        text1 = font.render("Bullets Remaining: " + str(bullets), True, (255, 255, 255))
    screen.blit(text1, (10, 750))

    font = pygame.font.Font('Fonts/Seaside.ttf', 40)
    if next_lvl and dead:
        text2 = font.render("Survival Time: "+ words, True, (255, 255, 255))
        text2_rect = text2.get_rect()

        # Center text on screen
        text2_rect.center = (screen.get_width() // 2, 150)
        screen.blit(text2, text2_rect)

    pygame.display.flip()



render()
running = True

while running:

    current_time = pygame.time.get_ticks()
    if bullets == 0 and did_reload == False:
        reload_channel.play(reload_sound)
        reload = True
        bullet_timer1 = pygame.time.get_ticks()
        did_reload = True

    if reload:
        if pygame.time.get_ticks() - bullet_timer1 > 2000:
            reload = False
            bullets = 7
            did_reload = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_r):
                reload = True
                bullet_timer1 = pygame.time.get_ticks()
                reload_channel.play(reload_sound)
            if (event.key == pygame.K_1):
                weapon = "pistol"
                player_group.sprites()[0].gun_image = pistol_img
            if (event.key == pygame.K_2):
                if has_shotgun == True:
                    weapon = "shotgun"
                    player_group.sprites()[0].gun_image = shotgun_img

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (bullets != -1):
                gunshot_channel.play(gunshot_sound);
                bullets -= 1


            for sprite in enemy_group.sprites():

                if not dead and sprite.rect.collidepoint(pygame.mouse.get_pos()):
                    if reload == False:
                        if current_time - last_click_time >= 300:
                            last_click_time = current_time
                            flash_sprite.rect.center = event.pos
                            flash_group.add(flash_sprite)
                            flash_timer = current_time
                            #CHANGE
                            if weapon == "shotgun":
                                sprite.health -= 30
                            elif weapon == "pistol":
                                sprite.health -=10

                    if sprite.health <= 0:
                        enemy_group.remove(sprite)
                        zombies_killed += 1
                        zombie_count -= 1
            if restart_sprite in button_group:
                if restart_sprite.rect.collidepoint(event.pos):
                    reset()
                    button_group.remove(restart_sprite)
                    button_group.empty()
                    dead = False

            if next_lvl_sprite in button_group and next_lvl_sprite.rect.collidepoint(event.pos):
                start_lvl = time.time()
                button_group.remove(next_lvl_sprite)
                button_group.empty()
                next_lvl = True
                bg_image = pygame.image.load('images/level2.png')
                time_elapsed = int(time.time() - start_lvl)
                draw_timer(time_elapsed, 700, 10)
                next_level = True
                start_time = pygame.time.get_ticks()
                create_zombie(7, 3, player_group.sprites()[0])
                timer = True

        if current_time - flash_timer >= 100:
            flash_group.empty()

        for sprite in loot_group.sprites():

            if sprite.rect.colliderect(player_group.sprites()[0]):
                pickUp_channel.play(pickUp_sound)
                loot_group.remove(sprite)
                loot_picked_up = True
                # shotgun
                if sprite.rect.width == 100:
                    player_group.sprites()[0].gun_image = shotgun_img
                    bullets = 7
                    has_shotgun = True
                    weapon = "shotgun"
                if sprite.rect.width == 50:
                    # healthpack
                    if (player_group.sprites()[0].health + 45 > player_group.sprites()[0].max_health):
                        player_group.sprites()[0].health = player_group.sprites()[0].max_health
                    else:
                        player_group.sprites()[0].health += 45
                if sprite.rect.width == 49:
                    # armor
                    player_group.sprites()[0].max_health += 30
                    player_group.sprites()[0].health += 30
                    player_group.sprites()[0].image = nate_tank_img
                    player_group.sprites()[0].image_path = 'images/HeavyNate.png'

    player_health = player_group.sprites()[0].health

    if not next_lvl and not dead:
        if (zombies_killed >= 2):
            num_normal = random.randint(0, 1)
            num_tank = 1 - num_normal
            enemy_group.add(create_zombie(num_normal, num_tank, player_group.sprites()[0]))
            zombies_killed = 0
            zombie_count += 1
            timer = False
    elif not dead:
        zombie_timer = pygame.time.get_ticks()
        if (zombie_timer - spawn_timer > 2000):
            num_normal = random.randint(0, 2)
            num_tank = 2 - num_normal
            enemy_group.add(create_zombie(num_normal, num_tank, player_group.sprites()[0]))
            zombies_killed = 0
            zombie_count += 1
            spawn_timer = zombie_timer
            timer = True

    # Load the images
    skull_img = pygame.image.load('images/skullandcrossbones.png')
    heart1_img = pygame.image.load('images/heart.png')
    heart2_img = pygame.image.load('images/heart2.png')
    heart3_img = pygame.image.load('images/heart3.png')
    heart4_img = pygame.image.load('images/heart4.png')

    # Define the image size tuples
    skull_size = (50, 50)
    heart1_size = (25, 25)
    heart2_size = (50, 25)
    heart3_size = (75, 25)
    heart4_size = (100, 25)

    # Determine which image to use based on player_health
    if player_health <= 0:
        health_img = skull_img
        health_size = skull_size
        dead = True
        weapon = "pistol"
        player_group.sprites()[0].gun_image = pistol_img
        if not death_sound_played:
            death_chanel.play(death_sound)
            death_sound_played = True

    elif player_health > 90:
        health_img = heart4_img
        health_size = heart4_size
    elif player_health >= 60:
        health_img = heart3_img
        health_size = heart3_size
    elif 30 <= player_health:
        health_img = heart2_img
        health_size = heart2_size
    else:
        health_img = heart1_img
        health_size = heart1_size

    if dead:
        button_group.add(restart_sprite)
        restart_sprite.rect.center = screen_rect.center
        timer = False

    health_img = pygame.transform.scale(health_img, health_size)
    health_rect = health_img.get_rect()

    render()
    clock.tick(60)
    if zombie_count == 0 and not next_lvl:
        button_group.add(next_lvl_sprite)
        loot_group.empty()
        next_lvl_sprite.rect.center = screen_rect.center

pygame.quit()
