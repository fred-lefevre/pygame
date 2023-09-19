#
# Initiation à Pygame - Épisode 13 - Jouer un son quand on presse une voyelle
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
pygame.display.set_caption("Épisode 13")
fen.fill(COULEUR_FOND)

pygame.mixer.init()

# Chargement du son
pygame.mixer.music.load("powerup2.mp3")

continuer = True

while continuer:
    
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
        elif event.type == pygame.TEXTINPUT:
            print(event.text, end = " ")
            if event.text in "aeiouy":
                pygame.mixer.music.play()

    pygame.display.flip()

# Libération des ressources utilisées pour le son
pygame.mixer.music.unload()

pygame.quit()
