#
# Initiation à Pygame - Épisode 17 - Afficher un compte à rebours
#
# https://kreatuto.info
#

import pygame

# Couleurs
ORANGE = (237, 127, 16)

# Couleur du fond de la fenête
COULEUR_FOND = (0, 255, 0)

# Couleur du score
COULEUR_COMPTEUR = (1, 49, 180)    # BLEU_SAPHIR

# Dimensions de la fenêtre
LARGEUR = 250
HAUTEUR = 100

# FPS = frame per second (images par seconde)
# Plus fps est élevé, moins il y aura d'attente entre deux rafraîchissements
# de l'affichage.
FPS = 1

pygame.init()

police = pygame.font.Font("SuperBubble-Rpaj3.ttf", 72)

# Documentation :
# https://www.pygame.org/docs/ref/time.html#pygame.time.Clock

# Permettra d'attendre avant de rafraîchir l'affichage
horloge = pygame.time.Clock()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 17")
fen.fill(COULEUR_FOND)

# Valeur initiale du compteur
compteur = 10

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False

    if compteur == 0:
        continuer = False

    # Mise à jour de l'affichage
    fen.fill(COULEUR_FOND)
    
    msg_compteur = police.render(f"{compteur:02d}", True, COULEUR_COMPTEUR)
    fen.blit(msg_compteur, (80, 20))

    pygame.display.flip()
    
    compteur -= 1
    
    # Documentation :
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    
    # Attente
    horloge.tick(FPS)

pygame.quit()
