#
# Initiation à Pygame - Épisode 7 - Afficher une image quand on clique
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
pygame.display.set_caption("Épisode 7")

# Chargement et préparation de l'image du petit panda
panda = pygame.image.load("panda-8171354_640.jpg").convert()
petit_panda = pygame.transform.scale(panda, (panda.get_width() // 3, panda.get_height() // 3))
petit_panda = petit_panda.convert()

# Gestion de l'état de l'affichage du panda
# True lorsque le panda est affiché, False sinon
afficher_panda = False

# Position du panda
position_panda = (0, 0)

continuer = True

while continuer:
    
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
        # L'utilisateur a-t-il enfoncé un bouton de souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            afficher_panda = True
            position_panda = event.pos
        
        elif event.type == pygame.MOUSEMOTION:
            position_panda = event.pos

        # L'utilisateur a-t-il enfoncé un bouton de souris
        elif event.type == pygame.MOUSEBUTTONUP:
            afficher_panda = False

    # La surface de la fenêtre est remplie avec sa couleur de fond.
    # Cela revient à supprimer tout ce qui aurait pu être affiché sur cette surface.
    fen.fill(COULEUR_FOND)
    
    if afficher_panda:
        fen.blit(petit_panda, position_panda)
    
    pygame.display.flip()


pygame.quit()
