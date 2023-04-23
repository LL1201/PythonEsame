from pathlib import Path
import pygame
import random
import Player
import Obstacle
import Menu


class Game():
    pointsRecord = 0

    def __init__(self):
        pygame.init()
        # parametri schermo
        self.screenW = 400
        self.screenH = 600
        self.screen = pygame.display.set_mode((self.screenW, self.screenH))
        pygame.display.set_caption('Gioco')

        # caricamento sprites di health
        # con conteggio per l'animazione
        self.healthSprites = [pygame.transform.scale(pygame.image.load(Path(
            f"images/assets/game/Health{i}.png")).convert_alpha(), (99, 33)) for i in range(1, 4)]
        self.currentHealthSprite = 0

        # parametri gestione etichetta punteggio
        self.font = pygame.font.SysFont("monospace", 30)
        self.pointsX = 320
        self.pointsY = 50

        # impostazione dell'immagine iniziale di health e posizionamento
        self.image = self.healthSprites[self.currentHealthSprite]
        self.rect = self.image.get_rect()
        self.healthX = 280
        self.healthY = 18
        self.points = 0

        # sprites player e ostacoli
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
        # estremi x
        xMin = -5
        xMax = 335

        for i in range(n):
            if i > 0:
                randPos = random.randint(xMin, xMax)
                tryCount = 0
                # se c'è più di un ostacolo, verifica la distanza
                # con quello precedente
                # se entro un ciclo non viene generata una nuova
                # coordinata x valida l'ostacolo viene posizionato fuori dallo schermo
                while abs(posx[-1] - randPos) < 100 and tryCount < 1:
                    randPos = random.randint(xMin, xMax)
                    tryCount += 1
                if tryCount == 1:
                    posx.append(500)
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
                properties["posx"][i], -100, self))

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
            # ad ogni iterazione viene aumentato di 0.025 in modo da generare
            # nuovi ostacoli ogni 40 iterazioni
            if int(self.newObstaclesCount) != 0:
                self.obstacles.add(self.generateObstacles())
                self.newObstaclesCount = 0
            self.newObstaclesCount += 0.025

            self.screen.fill((255, 255, 255))

            # input tasti e draw del player
            self.player.draw(self.screen)
            self.player.handleKeys()
            self.player.update()

            # draw dell'health e gestione punti
            self.screen.blit(
                self.healthSprites[self.currentHealthSprite], (self.healthX, self.healthY))
            self.label = self.font.render(str(self.points), 1, (0, 0, 0))
            self.screen.blit(self.label, (self.pointsX, self.pointsY))
            if self.points > Game.pointsRecord:
                Game.pointsRecord = self.points

            # draw del gruppo di ostacoli e aggiornamento con update
            # dell'animazione
            self.obstacles.draw(self.screen)
            self.obstacles.update()

            # se avviene una collisione tra il player e un qualsiasi ostacolo
            # viene incrementato il count delle collisioni e compare il menu di gameOver
            if pygame.sprite.spritecollide(self.player, self.obstacles, True, pygame.sprite.collide_mask):
                self.collisions += 1
                self.currentHealthSprite += 1
                if self.collisions == 3:
                    Menu.Menu(gameOver=True, points=self.points).startMenu()
                    self.player.kill()
            pygame.display.update()
            self.clock.tick(40)

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        self.__points = value
