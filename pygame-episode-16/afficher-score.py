#
# Initiation à Pygame - Épisode 16 - Afficher un score
#
# https://kreatuto.info
#

import pygame
import random

# Couleurs
ORANGE = (237, 127, 16)

# Couleur du fond de la fenête
COULEUR_FOND = (0, 255, 0)

# Couleur du score
SCORE_FOND  = (211, 211, 211) # GRIS_CLAIR
SCORE_TEXTE = (1, 49, 180)    # BLEU_SAPHIR

# Dimensions de la fenêtre
LARGEUR = 500
HAUTEUR = 350

pygame.init()

TAILLE_POLICE = 24
police = pygame.font.Font("SuperBubble-Rpaj3.ttf", TAILLE_POLICE)

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 16")
fen.fill(COULEUR_FOND)

LARGEUR_REC = 100
HAUTEUR_REC = 60

# Créer les rectangles
rectangles = list()
for _ in range(5):
    rectangles.append(pygame.Rect(20 + random.randint(0, 380), 20 + random.randint(0, 220), LARGEUR_REC, HAUTEUR_REC))

score = 0

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
                    score += 2500
    
    # Mise à jour de l'affichage
    fen.fill(COULEUR_FOND)
    
    pygame.draw.rect(fen, SCORE_FOND, [0, HAUTEUR - 50, LARGEUR, 50])
    
    # score sur 6 caractères avec des 0 en prefixe
    msg_score = police.render(f"{score:06d}", True, SCORE_TEXTE)
    largeur_msg, _ = msg_score.get_size()
    
    # Affichage centré du score
    fen.blit(msg_score, ((LARGEUR - largeur_msg) // 2, HAUTEUR - 50 + (50 - TAILLE_POLICE) // 2))
    
    for rect in rectangles:
        pygame.draw.rect(fen, ORANGE, rect)

    pygame.display.flip()

pygame.quit()
