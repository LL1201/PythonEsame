import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load(
            "images\\assets\\fireball\\FB500-1.png").convert_alpha())
        self.sprites.append(pygame.image.load(
            "images\\assets\\fireball\\FB500-2.png").convert_alpha())
        self.sprites.append(pygame.image.load(
            "images\\assets\\fireball\\FB500-3.png").convert_alpha())
        self.sprites.append(pygame.image.load(
            "images\\assets\\fireball\\FB500-4.png").convert_alpha())
        self.sprites.append(pygame.image.load(
            "images\\assets\\fireball\\FB500-5.png").convert_alpha())
        self.sprites.append(pygame.image.load(
            "images\\assets\\fireball\\B500-2.png"))
        self.sprites.append(pygame.image.load(
            "images\\assets\\fireball\\B500-3.png"))
        self.sprites.append(pygame.image.load(
            "images\\assets\\fireball\\B500-4.png"))
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [posx, posy]
        self.mask = pygame.mask.from_surface(self.sprites[0])

        self.w, self.h = pygame.display.get_surface().get_size()
        self.x = posx
        self.y = posy
        self.explodes = False

    def move(self):
        self.y += 4
        self.rect.topleft = [self.x, self.y]
        if self.y == 500:
            self.explodes = True
            self.currentSprite = 5

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.move()
        self.currentSprite += 0.5

        if self.currentSprite >= 4 and not self.explodes:
            self.currentSprite = 0
        elif self.currentSprite >= 7 and self.explodes:
            self.kill()

        self.image = self.sprites[int(self.currentSprite)]
