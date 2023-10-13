#
# Initiation à Pygame - Épisode 22 - Faire défiler une image
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
pygame.display.set_caption("Épisode 22")
fen.fill(COULEUR_FOND)

# Documentation :
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_alpha

# Préparation du fond pour son utilisation avec Pygame
fond_marin = fond_marin.convert()
fond_marin.set_alpha(96)

# Documentation :
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha

poisson = pygame.image.load("clip-art-3418189_250.png").convert_alpha()
LARGEUR_POISSON = poisson.get_width()

continuer = True

# Coordonnées du poisson
pos_x, pos_y = -LARGEUR_POISSON, 400

# Vitesse de déplacement du poisson
VITESSE_X = 5

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
    pos_x += VITESSE_X
    if pos_x >= LARGEUR:
        pos_x = -LARGEUR_POISSON

    # Mise à jour de l'affichage
    fen.fill(COULEUR_FOND)

    # Affichage du fond marin
    fen.blit(fond_marin, (0, 0))

    fen.blit(poisson, (pos_x, pos_y))

    pygame.display.flip()

    # Attente
    horloge.tick(FPS)

pygame.quit()
