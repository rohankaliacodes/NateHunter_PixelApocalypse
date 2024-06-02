import pygame, time


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, player, health, speed, damage, type, image):
        super().__init__()
        self.player = player
        self.image = image
        self.rect = self.image.get_rect()
        self.image_left = self.image
        self.image_right = pygame.transform.flip(self.image, True, False)
        self.rect.x = x
        self.rect.y = y
        self.health = health
        self.speed = speed
        self.type = type
        self.last_move_time = 0
        self.damage = damage

    def move(self):
        # Get the current time in seconds
        current_time = time.time()

        # Check if enough time has elapsed since the last move
        if current_time - self.last_move_time >= .05:
            if self.rect.x in range(self.player.rect.x - 5, self.player.rect.x + 5) and self.rect.y in range(
                    self.player.rect.y - 5, self.player.rect.y + 5):
                self.player.health -= self.damage
            else:
                if self.player.rect.x > self.rect.x:
                    self.image = self.image_right
                    self.rect.x += self.speed
                if self.player.rect.x < self.rect.x:
                    self.image = self.image_left
                    self.rect.x -= self.speed
                if self.player.rect.y > self.rect.y:
                    self.rect.y += self.speed
                if self.player.rect.y < self.rect.y:
                    self.rect.y -= self.speed

            # Update the time of the last move to the current time
            self.last_move_time = current_time

    def update(self):
        count = 0
        while count < 5:
            count += 0.001
        self.move()
