#
# Initiation à Pygame - Épisode 24 - Choisir dynamiquement un personnage
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
fond_sand = pygame.image.load("seychelles-4245171_711.jpg")

# Les dimensions de la fenêtre sont celles du trottoir
LARGEUR, HAUTEUR = fond_sand.get_size()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 24")
fen.fill(COULEUR_FOND)

# Préparation du fond pour son utilisation avec Pygame
fond_sand = fond_sand.convert()
fond_sand.set_alpha(200)

# Diviseur de la taille des images de personnage
DIV_PERSO = 2

# Récupération des dimensions d'un sprite
# Tous les sprites ont les mêmes dimensions
un_sprite = pygame.image.load("./dog/Walk (1).png")
LARGEUR_PERSO, HAUTEUR_PERSO = (int(un_sprite.get_width() / DIV_PERSO), int(un_sprite.get_height() / DIV_PERSO))
del un_sprite

# Nombre de sprites du personnage
NB_SPRITES_PERSO = 10

# Liste des personnages disponibles
# Ces noms sont également le nom des dossiers contenant les sprites
PERSO_DISPO = ['dog', 'cat']

# Dictionnaire des sprites de tous les personnages
perso = {}
for un_perso in PERSO_DISPO:
    # Comme les sprites sont numérotés de 1 à 10, on conserve cette numérotation
    # et l'incide 0 est inutilisé.
    perso[un_perso] = [None]
    for n in range(1, NB_SPRITES_PERSO + 1):
        # Préparation de l'image du sprite n du personnage
        img = pygame.image.load(f"./{un_perso}/Walk ({n:d}).png").convert_alpha()
        img = pygame.transform.scale(img, (LARGEUR_PERSO, HAUTEUR_PERSO))
        perso[un_perso].append(img)

continuer = True

# Numéro du personnage affiché
num_perso = 0

# Numéro du sprite
num_sprite = 1

# Coordonnées du personnage
pos_x, pos_y = -LARGEUR_PERSO, 25 + (HAUTEUR - HAUTEUR_PERSO) // 2

# Vitesse de déplacement du personnage
VITESSE_X = 6

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
        # L'utilisateur a-t-il relâché un bouton de souris
        elif event.type == pygame.MOUSEBUTTONUP:
            num_perso += 1
            if num_perso == len(PERSO_DISPO):
                num_perso = 0

    # Mise à jour de la position horizontale du personnage
    pos_x += VITESSE_X
    if pos_x >= LARGEUR:
        pos_x = -LARGEUR_PERSO
    
    # Changement du sprite utilisé comme image du personnage
    num_sprite += 1
    if num_sprite > NB_SPRITES_PERSO:
        num_sprite = 1

    # Mise à jour de l'affichage
    fen.fill(COULEUR_FOND)

    # Affichage du fond
    fen.blit(fond_sand, (0, 0))

    # Affichage du sprite du personnage à la nouvelle position
    fen.blit(perso[PERSO_DISPO[num_perso]][num_sprite], (pos_x, pos_y))

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Attente
    horloge.tick(FPS)

pygame.quit()
