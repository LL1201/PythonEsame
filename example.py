import pygame
import os
import random

clock = pygame.time.Clock()


playerImage = pygame.image.load(os.path.join('images', 'player.png'))
obstacleImage = pygame.image.load(os.path.join('images', 'putin.png'))


class Obstacle(object):
    def __init__(self, posx, posy):
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


class Player(object):
    def __init__(self):
        self.image = pygame.transform.scale(
            playerImage, (playerImage.get_rect().width/6, playerImage.get_rect().height/6))

        self.w, h = pygame.display.get_surface().get_size()
        self.x = self.w/2 - playerImage.get_rect().width/12
        self.y = h - playerImage.get_rect().height/6

    def handle_keys(self):
        try:
            key = pygame.key.get_pressed()
            dist = 10
            if key[pygame.K_RIGHT] and self.x < self.w-playerImage.get_rect().width/6:
                self.x += dist  # move right
            elif key[pygame.K_LEFT] and self.x > 0:
                self.x -= dist
        except:
            print("Exit")

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


def randomObstacle():
    return random.randint(0, 2)


pygame.init()
screen = pygame.display.set_mode((400, 600))

player = Player()
obstacles = [Obstacle(0, -100), Obstacle(200, -100), Obstacle(300, -100)]
rand = randomObstacle()

running = True

while running:
    screen.blit(pygame.image.load(os.path.join(
        'images', 'background.jpg')), (400, 600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    if not running:
        break
    player.handle_keys()

    player.draw(screen)
    obstacles[rand].draw(screen)
    obstacles[rand].move()
    pygame.display.update()

    clock.tick(40)
