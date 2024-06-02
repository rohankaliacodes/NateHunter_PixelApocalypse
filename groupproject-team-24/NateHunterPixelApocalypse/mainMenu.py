import pygame, sys
from button import Button
import game
import Enemy
import NateHunter

pygame.init()
pygame.mixer.init()
icon = pygame.image.load("images/gameIcon.png")
pygame.display.set_icon(icon)
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Nate Hunter: Pixel Apocalypse")
BG = pygame.image.load("images/Background2.jpg")
pygame.display.set_icon(icon)
menu_music = pygame.mixer.music.load("Sounds/mainMenu.wav")


pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

if pygame.mixer.music.get_busy():
    print("Main Menu Music is Playing")
else:
    print("Main Menu Music is not playing")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Fonts/Minecraft.ttf", size)


def play():
    pygame.mixer.music.stop()
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        game.gameloop()

        #  for event in pygame.event.get():
        #      if event.type == pygame.QUIT:
        #          pygame.quit()
        #          sys.exit()
        #      if event.type == pygame.KEYDOWN:
        #          if event.key == pygame.K_ESCAPE:


        #PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        #PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        #SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        #PLAY_BACK = Button(image=None, pos=(640, 460),text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        #PLAY_BUTTON = Button(image=None, pos)

        #PLAY_BACK.changeColor(PLAY_MOUSE_POS)
       # PLAY_BACK.update(SCREEN)
       #
       #  for event in pygame.event.get():
       #      if event.type == pygame.QUIT:
       #          pygame.quit()
       #          sys.exit()
       #      if event.type == pygame.MOUSEBUTTONDOWN:
       #          #if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
       #              #main_menu()
       #          if PLAY_BUTTON.checkForInput(PLAY_MOUSE_POS):
       #              os.system("game.py")
       #              main_menu()
       #              pygame.quit()
       #              sys.exit()



        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("green")

        #OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
       #OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        #SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        #OPTIONS_TEXT = get_font(20).render("Move Up: W\nMove Down: S\nMove Left: A\nMove Right: D\nShoot: Left/Right Mouse Click\nReload: R\nPrimary Weapon: 1\nSecondary Weapon: 2", True, "Black")
        #OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        #SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        controls_font = get_font(45)
        move_up_text = controls_font.render("Move Up: W", True, "Black")
        move_down_text = controls_font.render("Move Down: S", True, "Black")
        move_left_text = controls_font.render("Move Left: A", True, "Black")
        move_right_text = controls_font.render("Move Right: D", True, "Black")
        shoot_text = controls_font.render("Shoot: Left/Right Mouse Click", True, "Black")
        reload_text = controls_font.render("Reload: R", True, "Black")
        primary_weapon_text = controls_font.render("Primary Weapon: 1", True, "Black")
        secondary_weapon_text = controls_font.render("Secondary Weapon: 2", True, "Black")

        # Blit each line of the controls text onto the screen
        SCREEN.blit(move_up_text, (640 - move_up_text.get_width() // 2, 200))
        SCREEN.blit(move_down_text, (640 - move_down_text.get_width() // 2, 240))
        SCREEN.blit(move_left_text, (640 - move_left_text.get_width() // 2, 280))
        SCREEN.blit(move_right_text, (640 - move_right_text.get_width() // 2, 320))
        SCREEN.blit(shoot_text, (640 - shoot_text.get_width() // 2, 360))
        SCREEN.blit(reload_text, (640 - reload_text.get_width() // 2, 400))
        SCREEN.blit(primary_weapon_text, (640 - primary_weapon_text.get_width() // 2, 440))
        SCREEN.blit(secondary_weapon_text, (640 - secondary_weapon_text.get_width() // 2, 480))


       # controls_text = "Move Up: W\nMove Down: S\nMove Left: A\nMove Right: D\nShoot: Left/Right Mouse Click\nReload: R\nPrimary Weapon: 1\nSecondary Weapon: 2"
        #print(controls_text)
        #CONTROLS_TEXT = get_font(35).render(controls_text, controls_text, True, "Black")
        #CONTROLS_RECT = CONTROLS_TEXT.get_rect(center= (640, 400))
       #SCREEN.blit(CONTROLS_TEXT,CONTROLS_RECT)


        OPTIONS_BACK = Button(image=None, pos=(75, 700),
                             text_input="BACK", font=get_font(50), base_color="White", hovering_color="Black")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    pygame.mixer.music.load("Sounds/mainMenu.wav")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("images/PlayRect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("images/OptionsRect.png"), pos=(640, 400),
                                text_input="CONTROLS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("images/QuitRect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("play clicked")
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("options clicked")
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("quit clicked")
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()