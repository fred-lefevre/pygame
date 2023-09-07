#
# Initiation à Pygame - Épisode 8 - Dessiner des formes géométriques
#
# https://kreatuto.info
#

import pygame
import math

# Couleurs
BLEU_SAPHIR = (1, 49, 180)
GRIS_CLAIR = (211, 211, 211)
LAVANDE = (150, 131, 236)
ROUGE_CERISE = (187, 11, 11)
VERT_CITRON = (158, 253, 56)

# Couleur du fond de la fenête
COULEUR_FOND = GRIS_CLAIR

# Dimensions de la fenêtre
LARGEUR = 500
HAUTEUR = 300

pygame.init()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 8")
fen.fill(COULEUR_FOND)

# Rectangle
pygame.draw.rect(fen, VERT_CITRON, [10, 10, 100, 50])

# Documentation
# https://www.pygame.org/docs/ref/draw.html#pygame.draw.line

# Ligne
pygame.draw.line(fen, ROUGE_CERISE, [10, 290], [50, 250])

# Ligne épaisse
pygame.draw.line(fen, ROUGE_CERISE, [50, 250], [100, 250], 5)

# Documentation :
# https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle

# Disque
pygame.draw.circle(fen, LAVANDE, [250, 80], 25)

# Cercle
pygame.draw.circle(fen, LAVANDE, [250, 180], 25, 5)

# Documentation :
# https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon

# Polygone à quatre côtés
pygame.draw.polygon(fen, LAVANDE, [(400, 180), (480, 210), (420, 250), (380, 220)])

# Documentation :
# https://www.pygame.org/docs/ref/draw.html#pygame.draw.ellipse

pygame.draw.ellipse(fen, VERT_CITRON, [420, 0, 80, 30])
pygame.draw.ellipse(fen, BLEU_SAPHIR, [450, 0, 20, 30])

# Documentation :
# https://www.pygame.org/docs/ref/draw.html#pygame.draw.arc

pygame.draw.arc(fen, BLEU_SAPHIR, [20, 100, 120, 80], 0, 3 * math.pi / 2, 5)
pygame.draw.arc(fen, ROUGE_CERISE, [20, 100, 120, 80], 3 * math.pi / 2, 0, 5)

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
    pygame.display.flip()

pygame.quit()
