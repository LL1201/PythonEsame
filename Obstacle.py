import pygame


class Obstacle(object):
    def __init__(self, posx, posy, obstacleImage):
        self.image = pygame.transform.scale(
            obstacleImage, (obstacleImage.get_rect().width/6, obstacleImage.get_rect().height/6))

        self.w, self.h = pygame.display.get_surface().get_size()
        self.x = posx
        self.y = posy

    def changePosition(self, newx, newy):
        self.x = newx
        self.y = newy

    def move(self):
        self.y += 2
        if self.y > self.h:
            self.changePosition(0, 100)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
