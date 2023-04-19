import pygame
import os
import random
import Player
import Obstacle

playerImage = pygame.image.load(os.path.join('images', 'player.png'))
clock = pygame.time.Clock()
running = True

# screen
screenW = 400
screenH = 600
screen = pygame.display.set_mode((screenW, screenH))


def randomObstacleProperties():
    n = random.randint(1, 2)
    posx = []

    for i in range(n):
        if i > 0:
            randPos = random.randint(-25, 250)
            if abs(posx[-1] - randPos) < 150:
                if randPos + 150 > screenW:
                    posx.append(randPos - 150)
                else:
                    posx.append(randPos + 150)
            posx.append(randPos)
        else:
            posx.append(random.randint(-25, 250))

    return {"n": n, "posx": posx}


def generateObstacles():
    properties = randomObstacleProperties()
    obstaclesList = []
    for i in range(properties["n"]):
        obstaclesList.append(Obstacle.Obstacle(properties["posx"][i], -100))

    return obstaclesList


pygame.init()

# sprites
player = Player.Player(playerImage)
obstacles = pygame.sprite.Group()
newObstaclesCount = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    if not running:
        break

    if int(newObstaclesCount) != 0:
        obstacles.add(generateObstacles())
        newObstaclesCount = 0
    newObstaclesCount += 0.02
    player.handle_keys()
    # screen.blit(pygame.image.load(os.path.join('images', 'background.jpg')), (0, 0))
    screen.fill((255, 255, 255))
    player.draw(screen)
    obstacles.draw(screen)
    obstacles.update()
    pygame.sprite.spritecollide(player, obstacles, True)
    pygame.display.update()

    clock.tick(40)
