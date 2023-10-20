#
# Initiation à Pygame - Épisode 25 - Changer la vitesse de déplacement
#
# https://kreatuto.info
#

import pygame

# Couleur du fond de la fenête
COULEUR_FOND = (255, 255, 255)

# Couleur de la zone de commande
COULEUR_FOND_CMD  = (211, 211, 211) # GRIS_CLAIR

# Couleur d'affichage du texte dans la zone de commande
COULEUR_TXT_CMD = (1, 49, 180)    # BLEU_SAPHIR

# Hauteur de la zone de commande
HAUTEUR_CMD = 100

# FPS = frame per second (images par seconde)
FPS = 25

pygame.init()

# Chargement de la police de caractères pour afficher la vitesse
TAILLE_POLICE = 48
police = pygame.font.Font("SuperBubble-Rpaj3.ttf", TAILLE_POLICE)

# Permettra d'attendre avant de rafraîchir l'affichage
horloge = pygame.time.Clock()

# Chargement de l'image du fond de la fenêtre
fond_mountain = pygame.image.load("mountains-757731_600.jpg")

# Les dimensions de la fenêtre sont celles de l'image de la montagne
LARGEUR, HAUTEUR = fond_mountain.get_size()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 25")
fen.fill(COULEUR_FOND)

# Préparation du fond pour son utilisation avec Pygame
fond_mountain = fond_mountain.convert()
fond_mountain.set_alpha(200)

# Préparation des boutons de commandes de la vitesse
# Les boutons ont les mêmes dimensions
btn_plus = pygame.image.load("./btn/plus_47x50_normal.png").convert_alpha()
btn_moins_on = pygame.image.load("./btn/minus_47x50_normal.png").convert_alpha()
btn_moins_off = pygame.image.load("./btn/minus_47x50_locked.png").convert_alpha()
LARGEUR_BTN, HAUTEUR_BTN = btn_plus.get_size()
DECALAGE_X_BTN = 200
POS_X_BTN_PLUS = LARGEUR - DECALAGE_X_BTN
POS_X_BTN_MOINS = DECALAGE_X_BTN - LARGEUR_BTN
POS_Y_BTN = HAUTEUR - HAUTEUR_CMD + (HAUTEUR_CMD - HAUTEUR_BTN) // 2
# Zone contenant chaque bouton de commande
zone_cmd_plus = pygame.Rect(POS_X_BTN_PLUS, POS_Y_BTN, LARGEUR_BTN, HAUTEUR_BTN)
zone_cmd_moins = pygame.Rect(POS_X_BTN_MOINS, POS_Y_BTN, LARGEUR_BTN, HAUTEUR_BTN)

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
pos_x = (LARGEUR-LARGEUR_CHIEN) // 2
pos_y = (HAUTEUR - HAUTEUR_CHIEN - HAUTEUR_CMD) // 2

# Vitesse de déplacement du chien
vitesse_x = 2

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
            
        # L'utilisateur a-t-il relâché un bouton de souris
        elif event.type == pygame.MOUSEBUTTONUP:
            if zone_cmd_plus.collidepoint(event.pos):
                vitesse_x += 1
            elif zone_cmd_moins.collidepoint(event.pos) and vitesse_x > 0:
                vitesse_x -= 1
                    
    # Mise à jour de la position horizontale du chien
    pos_x += vitesse_x
    if pos_x >= LARGEUR:
        pos_x = -LARGEUR_CHIEN
    
    # Changement du sprite utilisé comme image du chien
    if vitesse_x != 0:
        num_chien += 1
        if num_chien > NB_CHIENS:
            num_chien = 1

    # Mise à jour de l'affichage
    fen.fill(COULEUR_FOND)

    # Affichage du fond
    fen.blit(fond_mountain, (0, 0))

    # Affichage de la zone de commande
    pygame.draw.rect(fen, COULEUR_FOND_CMD, [0, HAUTEUR - HAUTEUR_CMD, LARGEUR, HAUTEUR_CMD])

    # Affichage de la vitesse actuelle
    msg_vitesse = police.render(str(vitesse_x), True, COULEUR_TXT_CMD)
    largeur_msg, _ = msg_vitesse.get_size()
    
    # Affichage centré de la vitesse
    fen.blit(msg_vitesse, ((LARGEUR - largeur_msg) // 2, HAUTEUR - HAUTEUR_CMD + (HAUTEUR_CMD - TAILLE_POLICE) // 2))

    # Affichage des boutons de commande de la vitesse
    fen.blit(btn_plus, (POS_X_BTN_PLUS, POS_Y_BTN))
    if vitesse_x > 0:
        fen.blit(btn_moins_on, (POS_X_BTN_MOINS, POS_Y_BTN))
    else:
        fen.blit(btn_moins_off, (POS_X_BTN_MOINS, POS_Y_BTN))

    # Affichage du sprite du chien à la nouvelle position
    fen.blit(chiens[num_chien], (pos_x, pos_y))

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Attente
    horloge.tick(FPS)

pygame.quit()
