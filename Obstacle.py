from pathlib import Path
import pygame
import Game


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, posx, posy, gameObject):
        super().__init__()
        self.sprites = []

        # carica in una lista tutte le sprite per l'animazione dell'ostacolo
        # utilizzando la libreria pathlib (vedi Player)
        self.sprites = [pygame.image.load(Path(
            f"images/assets/fireball/FB500-{i}.png")).convert_alpha() for i in range(1, 9)]

        # parametri di gestione animazioni
        self.currentSprite = 0
        self.explodes = False
        self.gameObject = gameObject

        # impostazione immagine iniziale con relativa maschera per le collisioni
        self.image = self.sprites[self.currentSprite]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.sprites[0])

        # posizionamento dell'ostacolo
        self.w, self.h = pygame.display.get_surface().get_size()
        self.rect.topleft = [posx, posy]
        self.x = posx
        self.y = posy

    # metodo per permettere all'ostacolo di muoversi
    def move(self):
        self.y += 4
        self.rect.topleft = [self.x, self.y]
        # appena le y sono a 500 l'ostacolo esplode
        if self.y == 400:
            self.explodes = True
            self.currentSprite = 5
            if self.x < 500:
                self.gameObject.points += 10

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    # metodo per l'animazione dell'ostacolo chiamato ad ogni tick
    # del temporizzatore
    def update(self):
        self.move()

        # vedi animazione del Player
        self.currentSprite += 0.5

        # se il count dell'animazione è maggiore o uguale a 4 e l'ostacolo
        # non è esploso viene azzerato per iniziare il ciclo
        if self.currentSprite >= 4 and not self.explodes:
            self.currentSprite = 0

        # altrimenti viene fatto esplodere
        elif self.currentSprite >= 7 and self.explodes:
            self.kill()

        self.image = self.sprites[int(self.currentSprite)]
