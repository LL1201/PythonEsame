import pygame
import Game


class Menu():
    def __init__(self, gameOver):
        pygame.init()

        # parametri schermo
        self.screenW = 400
        self.screenH = 600
        self.screen = pygame.display.set_mode((self.screenW, self.screenH))
        pygame.display.set_caption('Menu di Avvio')

        # parametri scritte
        self.font = pygame.font.Font(None, 50)
        self.gameOver = gameOver

        # parametri di gioco
        self.running = True

    # metodo di istanza che permette di avviare il menu
    def startMenu(self):
        # se gameOver è True significa che deve mostrare la schermata
        # con la possibilità di fare il restart o uscire
        # altrimenti il Menu mostra il testo del menu iniziale
        if self.gameOver:
            self.screen.blit(self.font.render(
                "GAME OVER", True, (255, 255, 255)), (100, 100))
            self.screen.blit(self.font.render(
                "Press Enter to Restart", True, (255, 255, 255)), (20, 140))
            play_text = self.font.render("Restart", True, (255, 255, 255))
        else:
            self.screen.blit(self.font.render(
                "Press Enter to Play", True, (255, 255, 255)), (50, 100))
            play_text = self.font.render("Play", True, (255, 255, 255))

        # disegna il tasto per il play o restart
        # a seconda della schermata di gameover posiziona la scritta
        # play o restart in una diversa posizione
        playButton = pygame.Rect(100, 250, 200, 50)
        pygame.draw.rect(self.screen, (0, 255, 0), playButton)
        self.screen.blit(play_text, (playButton.x +
                         40 if self.gameOver else 160, playButton.y + 7))

        # scritta per uscire
        exitText = self.font.render("Press Q to exit", True, (255, 255, 255))
        self.screen.blit(exitText, (80, 450))  # centraggio titolo

        # cilo per rilevare la pressione dei tasti "Enter" e "Q"
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    # preme Invio
                    if event.key == pygame.K_RETURN:
                        # inizia il gioco
                        Game.Game().startGame()
                        self.running = False
                        break

                    # preme Q
                    if event.key == pygame.K_q:
                        # esce dal gioco
                        pygame.quit()
                        quit()
            if self.running:
                pygame.display.update()
            else:
                break
