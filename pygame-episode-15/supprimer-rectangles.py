#
# Initiation à Pygame - Épisode 15 - Supprimer des rectangles quand on clique dessus
#
# https://kreatuto.info
#

import pygame
import random

# Couleurs
ORANGE = (237, 127, 16)

# Couleur du fond de la fenête
COULEUR_FOND = (0, 255, 0)

# Dimensions de la fenêtre
LARGEUR = 500
HAUTEUR = 300

pygame.init()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 15")
fen.fill(COULEUR_FOND)

LARGEUR_REC = 100
HAUTEUR_REC = 60

# Créer les rectangles
rectangles = list()
for _ in range(5):
    rectangles.append(pygame.Rect(20 + random.randint(0, 380), 20 + random.randint(0, 220), LARGEUR_REC, HAUTEUR_REC))

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
        # L'utilisateur a-t-il relâché un bouton de souris
        elif event.type == pygame.MOUSEBUTTONUP:
            for rect in rectangles:
                if rect.collidepoint(event.pos):
                    rectangles.remove(rect)
    
    # Mise à jour de l'affichage
    fen.fill(COULEUR_FOND)
    
    for rect in rectangles:
        pygame.draw.rect(fen, ORANGE, rect)

    pygame.display.flip()

pygame.quit()
