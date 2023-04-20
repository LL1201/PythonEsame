import pygame
pygame.init()

#dimensioni schermo
WINDOW_WIDTH = 400 
WINDOW_HEIGHT = 600


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Menu di Avvio')#nome della finestra

font = pygame.font.Font(None, 50) #importo font

#scritta iniziale
title = font.render("Press Enter to Play", True, (255, 255, 255))
window.blit(title, (50, 100)) #centraggio titolo

#tasto play 
play_button = pygame.Rect(100, 250, 200, 50) #centraggio sfondo bottone
pygame.draw.rect(window, (0, 255, 0), play_button) #scritta play dentro superficie bottone
play_text = font.render("Play", True, (255, 255, 255)) #scritta play
window.blit(play_text, (play_button.x + 60, play_button.y + 7)) #centraggio x y scritta play

#scritta per uscire
exit_text = font.render("Press Q to exit", True, (255, 255, 255))
window.blit(exit_text, (80, 450)) #centraggio titolo


#cilo while pre rilevare la pressione dei tasti "Enter" e "Q"
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: #preme Invio
                    pass #inizia il gioco
                if event.key == pygame.K_q: #preme Q
                    pygame.quit()
                    quit() #esce dal gioco

    pygame.display.update()
