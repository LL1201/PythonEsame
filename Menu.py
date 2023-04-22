import pygame
import Game


class Menu():
    def __init__(self):
        pygame.init()
        # parametri schermo
        self.screenW = 400
        self.screenH = 600
        self.screen = pygame.display.set_mode((self.screenW, self.screenH))
        pygame.display.set_caption('Menu di Avvio')
        self.font = pygame.font.Font(None, 50)
        self.title = self.font.render(
            "Press Enter to Play", True, (255, 255, 255))

    def startMenu(self):
        self.screen.blit(self.title, (50, 100))  # centraggio titolo

        # tasto play
        play_button = pygame.Rect(100, 250, 200, 50)
        # scritta play dentro superficie bottone
        pygame.draw.rect(self.screen, (0, 255, 0), play_button)
        play_text = self.font.render(
            "Play", True, (255, 255, 255))  # scritta play
        # centraggio x y scritta play
        self.screen.blit(play_text, (play_button.x + 60, play_button.y + 7))

        # scritta per uscire
        exit_text = self.font.render("Press Q to exit", True, (255, 255, 255))
        self.screen.blit(exit_text, (80, 450))  # centraggio titolo

        # cilo while pre rilevare la pressione dei tasti "Enter" e "Q"
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # preme Invio
                        Game.Game().startGame()  # inizia il gioco
                    if event.key == pygame.K_q:  # preme Q
                        pygame.quit()
                        quit()  # esce dal gioco

            pygame.display.update()
