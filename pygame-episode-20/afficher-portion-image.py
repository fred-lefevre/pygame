#
# Initiation à Pygame - Épisode 20 - Afficher une portion d'image
#
# https://kreatuto.info
#

import pygame

# Couleur du fond de la fenête
COULEUR_FOND = (200, 200, 200)

pygame.init()

# Les dimensions de la fenêtre
LARGEUR, HAUTEUR = 500, 460

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 20")
fen.fill(COULEUR_FOND)

une_image = pygame.image.load("undersea-2521142_320.png").convert()
LARGEUR_IMG, HAUTEUR_IMG = une_image.get_size()

# Documentation :
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit

fen.blit(une_image, ( 50, 10), [0,   0, 80, HAUTEUR_IMG])
fen.blit(une_image, (160, 10), [81,  0, 80, HAUTEUR_IMG])
fen.blit(une_image, (270, 10), [161, 0, 80, HAUTEUR_IMG])
fen.blit(une_image, (381, 10), [241, 0, 80, HAUTEUR_IMG])

# Documentation :
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.subsurface

portion_image = une_image.subsurface([0, HAUTEUR_IMG - 50, LARGEUR_IMG, 50])

fen.blit(portion_image, (90, 340))
fen.blit(portion_image, (90, 400))

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
    pygame.display.flip()

pygame.quit()
