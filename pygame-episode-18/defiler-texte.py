#
# Initiation à Pygame - Épisode 18 - Faire défiler un texte
#
# https://kreatuto.info
#

import pygame

# Couleurs
ORANGE = (237, 127, 16)

# Couleur du fond de la fenête
COULEUR_FOND = (0, 255, 0)

# Couleur du score
COULEUR_TEXTE = (1, 49, 180)    # BLEU_SAPHIR

# Dimensions de la fenêtre
LARGEUR = 500
HAUTEUR = 76

# FPS = frame per second (images par seconde)
FPS = 30

pygame.init()

police = pygame.font.Font("BahayaNgak-1GmJe.otf", 36)
msg = police.render("Bobby is coming!", True, COULEUR_TEXTE)
largeur_msg, hauteur_msg = msg.get_size()

# Permettra d'attendre avant de rafraîchir l'affichage
horloge = pygame.time.Clock()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 18")
fen.fill(COULEUR_FOND)

# Position initiale du texte
pos_x = 0

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False

    pos_x = (pos_x + 3) % LARGEUR

    # Mise à jour de l'affichage
    fen.fill(COULEUR_FOND)
    
    fen.blit(msg, (pos_x, 20))
    if pos_x + largeur_msg > LARGEUR:
        fin_largeur = pos_x + largeur_msg - LARGEUR
        fin_rect = pygame.Rect(largeur_msg - fin_largeur, 0, fin_largeur, hauteur_msg)
        fin_msg = msg.subsurface(fin_rect)
        fen.blit(fin_msg, (0, 20))

    pygame.display.flip()
    
    # Attente
    horloge.tick(FPS)
    
pygame.quit()
