#
# Initiation à Pygame - Épisode 10 - Afficher du texte
#
# https://kreatuto.info
#

import pygame

# Couleurs
BLEU_SAPHIR = (1, 49, 180)
ROUGE_CERISE = (187, 11, 11)

# Couleur du fond de la fenête
COULEUR_FOND = (211, 211, 211)

pygame.init()

# Dimensions de la fenêtre
LARGEUR = 350
HAUTEUR = 200

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 10")
fen.fill(COULEUR_FOND)

# Documentation :
# https://www.pygame.org/docs/ref/font.html#pygame.font.Font

# Préparation des polices utilisées pour l'affichage des textes
grande_police = pygame.font.Font("SuperBubble-Rpaj3.ttf", 48)
petite_police = pygame.font.Font("AAhaWow-2O1K8.ttf", 24)

# Documentation :
# https://www.pygame.org/docs/ref/font.html#pygame.font.Font.render

# Préparation du rendu des texte
msg_bonjour = grande_police.render("Bonjour", True, ROUGE_CERISE)
msg_prenom = petite_police.render("Bobby", True, BLEU_SAPHIR)

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
            
    # Affichage des messages
    fen.blit(msg_bonjour, (20, 20))
    fen.blit(msg_prenom, (20, 80))
    
    pygame.display.flip()

pygame.quit()
