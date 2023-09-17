#
# Initiation à Pygame - Épisode 2 - Afficher une première fenêtre
#
# https://kreatuto.info
#

# Importation du module pygame
import pygame

# Importation du module time
import time

# Couleur du fond de la fenête
# C'est un tuple composé de 3 nombres entiers compris entre 0 et 255
# (R, V, B) R pour Rouge, V pour Vert et B pour Bleu
COULEUR_FOND = (0, 255, 0)

# Dimensions de la fenêtre
LARGEUR = 500
HAUTEUR = 200

# Initialisation du module pygame
pygame.init()

# Documentation :
# https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode

# Initialisation des dimensions de la fenêtre
# La variable fen permettra d'afficher des informations ...
# L'argument fourni est un tuple (donc deux paires de parenthèses)
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))

# Titre de la fenêtre
pygame.display.set_caption("Épisode 2")

# Définition de la couleur de fond de la fenêtre
fen.fill(COULEUR_FOND)

# Actualisation de l'affichage
pygame.display.flip()

# Attente de trois secondes
time.sleep(3)

# Arrêt du processus Pygame
pygame.quit()
