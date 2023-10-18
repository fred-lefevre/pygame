#
# Initiation à Pygame - Épisode 23 - Utiliser des sprites
#
# https://kreatuto.info
#

import pygame

# Couleur du fond de la fenête
COULEUR_FOND = (255, 255, 255)

# FPS = frame per second (images par seconde)
FPS = 25

pygame.init()

# Permettra d'attendre avant de rafraîchir l'affichage
horloge = pygame.time.Clock()

# Chargement de l'image du fond de la fenêtre
fond_cobble = pygame.image.load("cobblestone-83089_600.jpg")

# Les dimensions de la fenêtre sont celles du trottoir
LARGEUR, HAUTEUR = fond_cobble.get_size()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 23")
fen.fill(COULEUR_FOND)

# Préparation du fond pour son utilisation avec Pygame
fond_cobble = fond_cobble.convert()
fond_cobble.set_alpha(200)

# Diviseur de la taille de l'image du chien
DIV_CHIEN = 2.5

# Préparation de l'image du premier sprite du chien
chien = pygame.image.load("./dog/Walk (1).png").convert_alpha()
LARGEUR_CHIEN, HAUTEUR_CHIEN = (int(chien.get_width() / DIV_CHIEN), int(chien.get_height() / DIV_CHIEN))
chien = pygame.transform.scale(chien, (LARGEUR_CHIEN, HAUTEUR_CHIEN))

# Nombre de sprites du chien
NB_CHIENS = 10

# Initialisation de la liste des sprites du chien
# Comme les sprites sont numérotés de 1 à 10, on conserve cette numérotation
# et l'incide 0 inutilisé.
chiens = [None, chien]
for n in range(2, NB_CHIENS + 1):
    # Préparation de l'image du sprite n du chien
    chien = pygame.image.load(f"./dog/Walk ({n:d}).png").convert_alpha()
    chien = pygame.transform.scale(chien, (LARGEUR_CHIEN, HAUTEUR_CHIEN))
    chiens.append(chien)

continuer = True

# Numéro du sprite
num_chien = 1

# Coordonnées du chien
pos_x, pos_y = -LARGEUR_CHIEN, (HAUTEUR - HAUTEUR_CHIEN) // 2

# Vitesse de déplacement du chien
VITESSE_X = 6

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
    # Mise à jour de la position horizontale du chien
    pos_x += VITESSE_X
    if pos_x >= LARGEUR:
        pos_x = -LARGEUR_CHIEN
    
    # Changement du sprite utilisé comme image du chien
    num_chien += 1
    if num_chien > NB_CHIENS:
        num_chien = 1

    # Mise à jour de l'affichage
    fen.fill(COULEUR_FOND)

    # Affichage du fond
    fen.blit(fond_cobble, (0, 0))

    # Affichage du sprite du chien à la nouvelle position
    fen.blit(chiens[num_chien], (pos_x, pos_y))

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Attente
    horloge.tick(FPS)

pygame.quit()
