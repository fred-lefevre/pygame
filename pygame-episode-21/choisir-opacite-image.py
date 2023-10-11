#
# Initiation à Pygame - Épisode 21 - Choisir la transparence ou l'opacité d'une image
#
# https://kreatuto.info
#

import pygame

# Couleur du fond de la fenête
COULEUR_FOND = (255, 255, 255)

# FPS = frame per second (images par seconde)
FPS = 30

pygame.init()

# Permettra d'attendre avant de rafraîchir l'affichage
horloge = pygame.time.Clock()

# Chargement de l'image du fond de la fenêtre
fond_marin = pygame.image.load("underwater-4286600_640.jpg")

# Les dimensions de la fenêtre sont celles de l'image du bambou
LARGEUR, HAUTEUR = fond_marin.get_size()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 21")
fen.fill(COULEUR_FOND)

# Préparation du fond pour son utilisation avec Pygame
fond_marin = fond_marin.convert()

# Documentation :
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_alpha

# Entre 0 (transparence totale) et 255 (aucune transparence)
fond_marin.set_alpha(127)

poisson = pygame.image.load("clip-art-3418189_250.png")
poisson_alpha = poisson.copy()

# Documentation :
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha

poisson = poisson.convert()
poisson_alpha = poisson_alpha.convert_alpha()

# Mise à jour de l'affichage
fen.fill(COULEUR_FOND)

# Affichage du fond marin
fen.blit(fond_marin, (0, 0))

fen.blit(poisson, (100, 250))
fen.blit(poisson_alpha, (100, 450))

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False

    pygame.display.flip()

    # Attente
    horloge.tick(FPS)

pygame.quit()
