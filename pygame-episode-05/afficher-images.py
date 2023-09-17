#
# Initiation à Pygame - Épisode 5 - Afficher des images
#
# https://kreatuto.info
#

import pygame

# Couleur du fond de la fenête
COULEUR_FOND = (0, 255, 0)

pygame.init()

# Documentation :
# https://www.pygame.org/docs/ref/image.html#pygame.image.load

# Chargement de l'image du bambou vert
bambou = pygame.image.load("bamboo-3028709_640.jpg")
print("Dimension de l'image du bambou", bambou.get_size())

# Les dimensions de la fenêtre sont celles de l'image du bambou
LARGEUR, HAUTEUR = bambou.get_size()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 5")
fen.fill(COULEUR_FOND)

# Préparation de de l'image du bambou à son utilisation dans pygame
bambou = bambou.convert()

# Chargement et préparation de l'image du panda
panda = pygame.image.load("panda-8171354_640.jpg").convert()
print("Dimension de l'image du panda", panda.get_size())

# Documentation :
# https://www.pygame.org/docs/ref/transform.html#pygame.transform.scale

petit_panda = pygame.transform.scale(panda, (panda.get_width() // 3, panda.get_height() // 3))
petit_panda = petit_panda.convert()

# Affichage du bambou aux coordonnées précisées en second argument
fen.blit(bambou, (0, 0))

fen.blit(petit_panda, (100, 50))
fen.blit(petit_panda, (350, 250))

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
    pygame.display.flip()

pygame.quit()
