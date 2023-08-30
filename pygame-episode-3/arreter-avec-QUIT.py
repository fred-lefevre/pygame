#
# Initiation à Pygame - Épisode 3 - Arrêter le script avec l'événement QUIT
#
# https://kreatuto.info
#

import pygame

# Couleur du fond de la fenête
COULEUR_FOND = (0, 255, 0)

# Dimensions de la fenêtre
LARGEUR = 500
HAUTEUR = 200

pygame.init()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 3")
fen.fill(COULEUR_FOND)

continuer = True

while continuer:
    
    # Documentation :
    # https://www.pygame.org/docs/ref/event.html#pygame.event.get
    
    for event in pygame.event.get():
        #print(event)
        
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
        
    # Actualisation de l'affichage
    pygame.display.flip()

pygame.quit()
