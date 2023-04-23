from pathlib import Path
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # carica in una lista tutte le sprite per le animazioni del giocatore
        # viene utilizzata la libreria Pathlib in modo da utilizzare percorsi
        # compatibili con varie piattaforme
        self.sprites = []
        self.sprites = [pygame.transform.scale(pygame.image.load(Path(
            f"images/assets/player/Idle{i}.png")).convert_alpha(), (160, 160)) for i in range(1, 5)]
        self.sprites += [pygame.transform.scale(pygame.image.load(Path(
            f"images/assets/player/Run{i}.png")).convert_alpha(), (160, 160)) for i in range(1, 9)]

        # parametri di gestione animazioni
        self.currentSprite = 0
        self.rightMove = False
        self.leftMove = False
        self.previousLeftMove = False

        # impostazione dell'immagine iniziale
        # con relativa maschera per le collisioni
        self.image = self.sprites[self.currentSprite]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # posizionamento del giocatore nel campo di gioco
        self.displayW, displayH = pygame.display.get_surface().get_size()
        self.x = self.displayW/2 - self.image.get_rect().width
        self.y = displayH - self.image.get_rect().height
        self.rect.topleft = [self.x, self.y]

    # metodo per la gestione dei tasti premuti
    def handleKeys(self):
        try:
            key = pygame.key.get_pressed()
            playerSpeed = 10

            # evita che il player vada fuori dallo schermo
            # il +50 è dovuto alla cornice del relativo sprite
            if key[pygame.K_RIGHT] and self.x < (self.displayW + 50)-self.image.get_rect().width:
                self.x += playerSpeed
                self.rect.topleft = [self.x, self.y]  # move right
                self.rightMove = True
                self.previousLeftMove = False
            elif key[pygame.K_LEFT] and self.x > -50:
                self.x -= playerSpeed
                self.rect.topleft = [self.x, self.y]
                self.leftMove = True
                self.previousLeftMove = True
            else:
                self.leftMove, self.rightMove = False, False
        except:
            print("Handle keys problem")

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    # metodo per l'aggiornamento delle animazioni del giocatore
    def update(self):
        # incremento del current sprite ad ogni tick del temporizzatore
        # in questo modo, facendo un parse con Int il giocatore è animato
        # più lentamente
        self.currentSprite += 0.3

        # se il player si muove a destra o a sinistra le animazioni
        # sono solo dalla 4 alla 7, cioè quelle di Run
        if self.rightMove or self.leftMove:
            if self.currentSprite < 4:
                self.currentSprite = 4

        # se il player è in Idle si evita che le animazioni superino la numero
        # 4, cioè l'ultima di Idle
        if self.currentSprite >= 4 and not (self.rightMove or self.leftMove):
            self.currentSprite = 0

        # invece, se il giocatore si muove le animazioni vanno dalla 4 alla 7
        # e qua si evita che il count superi la dimensione massima della lista
        elif self.currentSprite >= 7 and (self.rightMove or self.leftMove):
            self.currentSprite = 4

        # se il giocatore si muove a sinistra o si era mosso a sinistra
        # le sprite vengono specchiate in modo da posizionarle nella giusta
        # direzione di movimento
        if self.leftMove or self.previousLeftMove:
            self.image = pygame.transform.flip(
                self.sprites[int(self.currentSprite)], True, False)
        else:
            self.image = self.sprites[int(self.currentSprite)]

        # viene inoltre aggiornata la maschera con la nuova immagine
        self.mask = pygame.mask.from_surface(self.image)

    @ property
    def mask(self):
        return self.__mask

    @ mask.setter
    def mask(self, value):
        self.__mask = value
