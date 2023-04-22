import pygame
import random
import Player
import Obstacle

# parametri schermo
screenW = 400
screenH = 600
screen = pygame.display.set_mode((screenW, screenH))

# metodo che genera le proprietà degli ostacoli che devono comparire nel gioco


def randomObstacleProperties():
    # genera 1 o 2 ostacoli
    n = random.randint(1, 2)
    # vettore che contiene le posizioni degli ostacoli generati
    posx = []

    for i in range(n):
        if i > 0:
            randPos = random.randint(-25, 250)
            tryCount = 0
            # se c'è più di un ostacolo, verifica la distanza
            # con quello precedente
            # se entro un ciclo non viene generata una nuova
            # coordinata x valida l'ostacolo viene posizionato fuori dallo schermo
            while abs(posx[-1] - randPos) < 150 and tryCount < 1:
                randPos = random.randint(-25, 250)
                tryCount += 1
            if tryCount == 1:
                posx.append(400)
            else:
                posx.append(randPos)
        else:
            posx.append(random.randint(-25, 250))

    return {"n": n, "posx": posx}


# funzione che restituisce una lista degli ostacoli da aggiungere al campo di gioco
def generateObstacles():
    properties = randomObstacleProperties()
    obstaclesList = []
    # ciclo che genera gli ostacoli a seconda delle loro proprietà al di sopra dello schermo in modo che poi scendano
    for i in range(properties["n"]):
        obstaclesList.append(Obstacle.Obstacle(properties["posx"][i], -100))

    return obstaclesList


# sprites
player = Player.Player()
obstacles = pygame.sprite.Group()

# parametri loop di gioco
clock = pygame.time.Clock()
running = True
newObstaclesCount = 1
collisions = 0
pygame.init()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    if not running:
        break

    # aggiunge gli ostacoli generati al gruppo di sprite quando
    # il parsing Intero di newObstaclesCount è diverso da zero
    # ad ogni iterazione viene aumentato di 0.02 in modo da generare
    # nuovi ostacoli ogni 50 iterazioni
    if int(newObstaclesCount) != 0:
        obstacles.add(generateObstacles())
        newObstaclesCount = 0
    newObstaclesCount += 0.025

    screen.fill((255, 255, 255))

    # input tasti e draw del player
    player.draw(screen)
    player.handle_keys()
    player.update()

    # draw del gruppo di ostacoli e aggiornamento con update
    # dell'animazione
    obstacles.draw(screen)
    obstacles.update()

    # se avviene una collisione tra il player e un qualsiasi ostacolo
    # viene incrementato il count delle collisioni
    if pygame.sprite.spritecollide(player, obstacles, True, pygame.sprite.collide_mask):
        collisions += 1
        print(collisions)

    pygame.display.update()
    clock.tick(40)
