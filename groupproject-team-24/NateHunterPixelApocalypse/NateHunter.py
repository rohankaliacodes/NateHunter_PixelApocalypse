import pygame


# Define a Player class that inherits from the Pygame Sprite class
class Player(pygame.sprite.Sprite):
    # Constructor method that initializes the Player instance
    def __init__(self, screen, pos, groups, barrier_sprites, health):
        # Call the constructor of the parent class
        super().__init__(groups)
        # Load the player sprite image and set its position
        self.gun_image_flipped = None
        self.gun_rect = None
        self.screen = screen
        self.image = pygame.image.load('images/Nate.png')
        self.image_path = 'images/Nate.png'
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        # initialize gun attributes
        self.gun_image = pygame.image.load('images/pistol.png')
        self.gun_image = pygame.transform.flip(self.gun_image, True, False)
        self.gun_image = pygame.transform.scale(self.gun_image, (65, 65))
        self.gun_offset = pygame.math.Vector2(0, 0)  # set gun offset relative to player
        self.gun_angle = 0  # initial gun angle

        # Initialize the player's movement direction and speed
        self.direction = pygame.math.Vector2()
        self.speed = 4

        # Keep track of obstacle sprites to check for collisions
        self.barrier_sprites = barrier_sprites
        self.health = health
        self.max_health = 90

    # Method to draw the gun sprite on top of the player sprite
    def update_gun(self):
        # Get position of mouse pointer
        mouse_pos = pygame.mouse.get_pos()

        # Set gun angle based on position of mouse pointer
        if mouse_pos[0] < self.rect.centerx:
            self.gun_angle = 90
        else:
            self.gun_angle = -90

        # Set gun position relative to player
        self.gun_offset = pygame.math.Vector2(50, 10)
        gun_pos = self.rect.center + self.gun_offset
        self.gun_rect = self.gun_image.get_rect(center=gun_pos)

        # Determine if gun needs to be flipped based on direction
        if self.gun_angle > 0:
            self.gun_image_flipped = pygame.transform.flip(self.gun_image, True, False)
        else:
            self.gun_image_flipped = self.gun_image

        # Draw gun image on top of player image
        self.screen.blit(self.gun_image_flipped, self.gun_rect)

    # Method that reads keyboard input and updates the player's movement direction
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction = pygame.math.Vector2()

        if self.health > 0:

            if keys[pygame.K_w]:
                self.image = pygame.image.load(self.image_path)
                self.image = pygame.transform.scale(self.image, (125, 125))
                self.direction.y = -1
            elif keys[pygame.K_s]:
                self.image = pygame.image.load(self.image_path)
                self.image = pygame.transform.scale(self.image, (125, 125))
                self.direction.y = 1
            if keys[pygame.K_a]:
                self.image = pygame.image.load(self.image_path)
                self.image = pygame.transform.flip(pygame.transform.scale(self.image, (125, 125)), True, False)
                self.direction.x = -1
            elif keys[pygame.K_d]:
                self.image = pygame.image.load(self.image_path)
                self.image = pygame.transform.scale(self.image, (125, 125))
                self.direction.x = 1

    # Method that moves the player's sprite and checks for collisions with obstacles
    def move(self, speed):
        if self.direction.magnitude() != 0:
            # moves player at a constant speed instead of having them accelerate
            self.direction = self.direction.normalize()
        else:
            self.image = pygame.image.load(self.image_path)
            self.image = pygame.transform.scale(self.image, (125, 125))

        if 0 < self.rect.x < 800 - self.rect.width:
            self.rect.x += self.direction.x * speed
            self.check_collision('left/right')
        elif self.rect.x <= 0:
            self.rect.x = 5
        elif self.rect.x + self.rect.width >= 800:
            self.rect.x = 795 - self.rect.width

        if 150 < self.rect.y < 700 - self.rect.height:
            self.rect.y += self.direction.y * speed
            self.check_collision('up/down')
        elif self.rect.y <= 150:
            self.rect.y = 155
        elif self.rect.y + self.rect.height >= 700:
            self.rect.y = 695 - self.rect.height

    # Method that checks for collisions with obstacles in the given direction
    def check_collision(self, direction):
        for sprite in self.barrier_sprites:
            if self.rect.colliderect(sprite.rect):
                if direction == 'left/right':
                    if self.direction.x > 0:  # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # moving left
                        self.rect.left = sprite.rect.right
                if direction == 'up/down':
                    if self.direction.y > 0:  # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # moving up
                        self.rect.top = sprite.rect.bottom

    # Method that updates the player's sprite by reading input and moving it
    def update(self):

        self.input()
        self.move(self.speed)
        if self.health <= 0:
            self.image = pygame.transform.scale(pygame.image.load('images/death.png'), (100, 100))

        # Draw the gun on top of the player image
        self.update_gun()

        # Draw the player image on the screen
        self.screen.blit(self.image, self.rect)
