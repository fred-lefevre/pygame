#
# Initiation à Pygame - Épisode 12 - Jouer un son
#
# https://kreatuto.info
#

import pygame

# Couleur du fond de la fenête
COULEUR_FOND = (0, 255, 0)

# Dimensions de la fenêtre
LARGEUR = 500
HAUTEUR = 300

pygame.init()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 12")
fen.fill(COULEUR_FOND)

# Documentation :
#https://www.pygame.org/docs/ref/music.html

pygame.mixer.init()

# Chargement du son
pygame.mixer.music.load("167201__mitchthorne__cat-purring.mp3")
#pygame.mixer.music.load("jingle.wav")
#pygame.mixer.music.load("zap4", "ogg")

continuer = True

while continuer:
    
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Début de la diffusion du son
            pygame.mixer.music.play()

        elif event.type == pygame.MOUSEBUTTONUP:
            # Arrêt de la diffusion du son
            pygame.mixer.music.stop()

    pygame.display.flip()

# Libération des ressources utilisées pour le son
pygame.mixer.music.unload()

pygame.quit()
