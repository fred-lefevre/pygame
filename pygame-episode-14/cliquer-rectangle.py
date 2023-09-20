#
# Initiation à Pygame - Épisode 14 - Cliquer dans un rectangle ... ou non
#
# https://kreatuto.info
#

import pygame

# Couleurs
JAUNE = (255, 255, 0)
ORANGE = (237, 127, 16)

# Couleur du fond de la fenête
COULEUR_FOND = (0, 255, 0)

# Dimensions de la fenêtre
LARGEUR = 500
HAUTEUR = 300

pygame.init()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 14")
fen.fill(COULEUR_FOND)

# Documentation :
# https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect

LARGEUR_REC = 300
HAUTEUR_REC = 100

# Dessiner les deux rectangles
rect_orange = pygame.draw.rect(fen, ORANGE, [20, 20, LARGEUR_REC, HAUTEUR_REC])
rect_jaune  = pygame.draw.rect(fen, JAUNE,  [50, 80, LARGEUR_REC, HAUTEUR_REC])

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
        # L'utilisateur a-t-il relâché un bouton de souris
        elif event.type == pygame.MOUSEBUTTONUP:
            print("up", event.pos)
            if rect_jaune.collidepoint(event.pos):
                print(" --> Jaune")
                
            if rect_orange.collidepoint(event.pos):
                print(" --> Orange")
                
            if rect_jaune.collidepoint(event.pos) and rect_orange.collidepoint(event.pos):
                print(" --> Jaune et Orange")
    
    pygame.display.flip()

pygame.quit()
