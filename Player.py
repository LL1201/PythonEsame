import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.transform.scale(
        #    playerImage, (playerImage.get_rect().width/6, playerImage.get_rect().height/6))
        self.image = pygame.image.load(
            "images\\assets\\player\\player.png").convert_alpha()

        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.displayW, displayH = pygame.display.get_surface().get_size()
        self.x = self.displayW/2 - self.image.get_rect().width
        self.y = displayH - self.image.get_rect().height
        self.rect.topleft = [self.x, self.y]
        self.mask = pygame.mask.from_surface(self.image)

    def handle_keys(self):
        try:
            key = pygame.key.get_pressed()
            dist = 10
            if key[pygame.K_RIGHT] and self.x < self.displayW-self.image.get_rect().width:
                self.x += dist
                self.rect.topleft = [self.x, self.y]  # move right
            elif key[pygame.K_LEFT] and self.x > 0:
                self.x -= dist
                self.rect.topleft = [self.x, self.y]
        except:
            print("Exit")

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
