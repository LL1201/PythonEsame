import pygame


class Player(object):
    def __init__(self, playerImage):
        self.image = pygame.transform.scale(
            playerImage, (playerImage.get_rect().width/6, playerImage.get_rect().height/6))

        self.displayW, displayH = pygame.display.get_surface().get_size()
        self.x = self.displayW/2 - playerImage.get_rect().width/12
        self.y = displayH - playerImage.get_rect().height/6

    def handle_keys(self):
        try:
            key = pygame.key.get_pressed()
            dist = 10
            if key[pygame.K_RIGHT] and self.x < self.displayW-self.image.get_rect().width:
                self.x += dist  # move right
            elif key[pygame.K_LEFT] and self.x > 0:
                self.x -= dist
        except:
            print("Exit")

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
