#
# Initiation à Pygame - Épisode 11 - Réagir aux événements clavier
#
# https://kreatuto.info
#

import pygame

# Couleur du fond de la fenête
COULEUR_FOND = (0, 255, 0)

# Dimensions de la fenêtre
LARGEUR = 500
HAUTEUR = 300

pygame.init()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Épisode 11")
fen.fill(COULEUR_FOND)

# Documentation :
# https://www.pygame.org/docs/ref/key.html

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
        
        # L'utilisateur a-t-il saisit un caractère ?
        elif event.type == pygame.TEXTINPUT:
            print("textinput", event.text)

        # L'utilisateur a-t-il pressé une touche
        elif event.type == pygame.KEYDOWN:
            if event.unicode == '':
                # K_DOWN K_RIGHT K_LEFT
                if event.key == pygame.K_UP:
                    print("down Flèche vers le haut")
                # K_RSHIFT
                elif event.key == pygame.K_LSHIFT:
                    print("down Shitf gauche")
                else:
                    print("down", event.key)
                
                if event.mod & pygame.KMOD_SHIFT:
                    print("down shift droit ou gauche")
            else:
                print("down", event.unicode, event.key)
        
        # L'utilisateur a-t-il relâché une touche
        elif event.type == pygame.KEYUP:
            if event.unicode == '':
                pass
            else:
                print("up", event.unicode, event.key)
            
    pygame.display.flip()

pygame.quit()
