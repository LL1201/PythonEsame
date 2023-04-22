import pygame
import random
import Player
import Obstacle
import Menu


class Game():
    def __init__(self):
        pygame.init()
        # parametri schermo
        self.screenW = 400
        self.screenH = 600
        self.screen = pygame.display.set_mode((self.screenW, self.screenH))
        pygame.display.set_caption('Gioco')

        # sprites
        self.player = Player.Player()
        self.obstacles = pygame.sprite.Group()

        # parametri loop di gioco
        self.clock = pygame.time.Clock()
        self.running = True
        self.newObstaclesCount = 1
        self.collisions = 0

    # metodo che genera le proprietà degli ostacoli che devono comparire nel gioco

    def randomObstacleProperties(self):
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

    def generateObstacles(self):
        properties = self.randomObstacleProperties()
        obstaclesList = []
        # ciclo che genera gli ostacoli a seconda delle loro proprietà al di sopra dello schermo in modo che poi scendano
        for i in range(properties["n"]):
            obstaclesList.append(Obstacle.Obstacle(
                properties["posx"][i], -100))

        return obstaclesList

    def startGame(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False

            if not self.running:
                break

            # aggiunge gli ostacoli generati al gruppo di sprite quando
            # il parsing Intero di newObstaclesCount è diverso da zero
            # ad ogni iterazione viene aumentato di 0.02 in modo da generare
            # nuovi ostacoli ogni 50 iterazioni
            if int(self.newObstaclesCount) != 0:
                self.obstacles.add(self.generateObstacles())
                self.newObstaclesCount = 0
            self.newObstaclesCount += 0.025

            self.screen.fill((255, 255, 255))

            # input tasti e draw del player
            self.player.draw(self.screen)
            self.player.handle_keys()
            self.player.update()

            # draw del gruppo di ostacoli e aggiornamento con update
            # dell'animazione
            self.obstacles.draw(self.screen)
            self.obstacles.update()

            # se avviene una collisione tra il player e un qualsiasi ostacolo
            # viene incrementato il count delle collisioni
            if pygame.sprite.spritecollide(self.player, self.obstacles, True, pygame.sprite.collide_mask):
                self.collisions += 1
                if self.collisions == 3:
                    Menu.Menu(True).startMenu()
                    self.player.kill()
                    self.kill()
            pygame.display.update()
            self.clock.tick(40)
