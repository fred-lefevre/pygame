#
# Initiation à Pygame - Épisode 6 - Réagir aux événements souris
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
pygame.display.set_caption("Épisode 6")
fen.fill(COULEUR_FOND)

# Documentation :
# https://www.pygame.org/docs/ref/event.html#pygame.event.get

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False

        # L'utilisateur a-t-il enfoncé un bouton de souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("down", event.pos)
        
        # L'utilisateur a-t-il relâché un bouton de souris
        elif event.type == pygame.MOUSEBUTTONUP:
            print("up", event.pos)
        
        # L'utilisateur a-t-il déplacé sa souris
        elif event.type == pygame.MOUSEMOTION:
            print("motion", event.pos)
        
        elif event.type == pygame.MOUSEWHEEL:
            print("wheel", event.x, event.y)
            
    pygame.display.flip()

pygame.quit()
