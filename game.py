import pygame
import os
import random
import Player
import Obstacle

playerImage = pygame.image.load(os.path.join('images', 'player.png'))
obstacleImage = pygame.image.load(os.path.join('images', 'putin.png'))
clock = pygame.time.Clock()
running = True


def randomObstacle():
    return random.randint(0, 2)


pygame.init()
screen = pygame.display.set_mode((400, 600))

player = Player.Player(playerImage)
obstacles = [Obstacle.Obstacle(0, -100, obstacleImage),
             Obstacle.Obstacle(200, -100, obstacleImage), Obstacle.Obstacle(300, -100, obstacleImage)]
rand = randomObstacle()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    if not running:
        break
    player.handle_keys()
    screen.blit(pygame.image.load(os.path.join(
        'images', 'background.jpg')), (0, 0))
    player.draw(screen)
    obstacles[rand].draw(screen)
    obstacles[rand].move()
    pygame.display.update()

    clock.tick(40)
