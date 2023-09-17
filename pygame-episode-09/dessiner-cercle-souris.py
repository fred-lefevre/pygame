#
# Initiation à Pygame - Épisode 9 - Dessiner un cercle avec la souris
#
# https://kreatuto.info
#

import pygame
import math

ROUGE = (255, 0, 0)

# Couleur du fond de la fenête
COULEUR_FOND = (0, 255, 0)

# Dimensions de la fenêtre
LARGEUR = 500
HAUTEUR = 300

pygame.init()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 9")

# Gestion de l'état de l'affichage du cercle
# True lorsque le cercle est affiché, False sinon
afficher_cercle = False

# Position du centre du cercle
centre = (0, 0)

# Rayon du cercle
rayon = 0

continuer = True

while continuer:
    
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
        # L'utilisateur a-t-il enfoncé un bouton de souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            afficher_cercle = True
            centre = event.pos
            rayon = 0
        
        elif event.type == pygame.MOUSEMOTION:
            rayon = math.sqrt(math.pow(centre[0] - event.pos[0], 2) + math.pow(centre[1] - event.pos[1], 2))

        # L'utilisateur a-t-il enfoncé un bouton de souris
        elif event.type == pygame.MOUSEBUTTONUP:
            afficher_cercle = False

    # La surface de la fenêtre est remplie avec sa couleur de fond.
    # Cela revient à supprimer tout ce qui aurait pu être affiché sur cette surface.
    fen.fill(COULEUR_FOND)
    
    if afficher_cercle:
        pygame.draw.circle(fen, ROUGE, centre, rayon)
    
    pygame.display.flip()


pygame.quit()
