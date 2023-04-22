import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.transform.scale(
        #    playerImage, (playerImage.get_rect().width/6, playerImage.get_rect().height/6))
        self.sprites = []
        self.sprites = [pygame.transform.scale(pygame.image.load(
            f"images\\assets\\player\\Idle{i}.png").convert_alpha(), (160, 160)) for i in range(1, 5)]
        self.sprites += [pygame.transform.scale(pygame.image.load(
            f"images\\assets\\player\\Run{i}.png").convert_alpha(), (160, 160)) for i in range(1, 9)]

        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]

        self.rightMove = False
        self.leftMove = False
        self.previousLeftMove = False

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
            if key[pygame.K_RIGHT] and self.x < (self.displayW + 50)-self.image.get_rect().width:
                self.x += dist
                self.rect.topleft = [self.x, self.y]  # move right
                self.rightMove = True
                self.previousLeftMove = False
            elif key[pygame.K_LEFT] and self.x > -50:
                self.x -= dist
                self.rect.topleft = [self.x, self.y]
                self.leftMove = True
                self.previousLeftMove = True
            else:
                self.leftMove, self.rightMove = False, False
        except:
            print("Exit")

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.currentSprite += 0.3

        if self.rightMove or self.leftMove:
            if self.currentSprite < 4:
                self.currentSprite = 4

        if self.currentSprite >= 4 and not (self.rightMove or self.leftMove):
            self.currentSprite = 0
        elif self.currentSprite >= 7 and (self.rightMove or self.leftMove):
            self.currentSprite = 4

        if self.leftMove or self.previousLeftMove:
            self.image = pygame.transform.flip(
                self.sprites[int(self.currentSprite)], True, False)
        else:
            self.image = self.sprites[int(self.currentSprite)]
        self.mask = pygame.mask.from_surface(self.image)

    @ property
    def mask(self):
        return self.__mask

    @ mask.setter
    def mask(self, value):
        self.__mask = value
