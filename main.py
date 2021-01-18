import pygame

import random

from src.Panier import Panier

from src.OeufChocolat import OeufChocolat


print(" ============================================ ")
print(" By Kyrokx()#7573 🦊 ")
print(" ============================================ ")

# Initier le module pygame
pygame.init()

# Information de la fenêtre [
pygame.display.set_caption(" Easter Bunny ")
pygame.display.set_icon(pygame.image.load('assets/carrot.png'))
screen = pygame.display.set_mode((800 , 480))

largeur = random.randint(0 , 470)
hauteur = 0
# ]

# Les images [
background = pygame.image.load('assets/fond.jpg')
ground = pygame.image.load('assets/sol.png')
# ]
run = True
pressed = {}

player = Panier()

Egg = OeufChocolat(largeur, hauteur, player)
oeufs = pygame.sprite.Group()

# Boucle qui s'exetue [
while run:
    oeufs.add(Egg)
    oeufs.add(Egg)
    # Appliquer le fond
    screen.blit(background , (0 , 0))

    # Appliquer le sol
    screen.blit(ground , (0 , 0))

    # Appliquer l'image du player
    screen.blit(player.image , player.rect)

    oeufs.draw(screen)


    # Mouvement du joueur
    if pressed.get(pygame.K_RIGHT) and player.rect.x + player.rect.width < screen.get_width():
        player.move_right()
    elif pressed.get(pygame.K_LEFT) and player.rect.x > 0:
        player.move_left()        


    for oeuf in oeufs:
        oeuf.gravity()

    # Mettre a jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        import time

        # l'evenement est la fermeture de la fenetre
        if event.type == pygame.QUIT:
            time.sleep(0.5)
            run = False
            pygame.quit()
            print(" ⏳ ... Entrain de se fermer !... ")

            time.sleep(1)
            print(" ❌ Fermeture de la fenêtre PyGame ! ")

        elif event.type == pygame.KEYDOWN:
            pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            pressed[event.key] = False
# ]