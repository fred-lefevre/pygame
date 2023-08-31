#
# Initiation à Pygame - Épisode 4 - Dessiner des rectangles
#
# https://kreatuto.info
#

import pygame

# Couleurs
JAUNE = (255, 255, 0)
ORANGE = (237, 127, 16)
VIOLET = (128,  0, 128)

# Couleur du fond de la fenête
COULEUR_FOND = (0, 255, 0)

# Dimensions de la fenêtre
LARGEUR = 500
HAUTEUR = 300

pygame.init()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 4")
fen.fill(COULEUR_FOND)

# Documentation :
# https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect

LARGEUR_REC = 100
HAUTEUR_REC = 50

# Trois arguments obligatoires :
# 1) la surface dans laquelle est dessinée le rectangle
# 2) la couleur
# 3) Coordonnées suivies de la largeur puis de la hauteur
pygame.draw.rect(fen, ORANGE, [10, 10, LARGEUR_REC, HAUTEUR_REC])

pygame.draw.rect(fen, JAUNE, [LARGEUR - 10 - LARGEUR_REC, 10, LARGEUR_REC, HAUTEUR_REC])

# 4) l'épaisseur du trait
pygame.draw.rect(fen, VIOLET, [150, 150, LARGEUR_REC, HAUTEUR_REC], 5)

pygame.draw.rect(fen, JAUNE, [40, 40, LARGEUR_REC, HAUTEUR_REC])

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
    pygame.display.flip()

pygame.quit()
