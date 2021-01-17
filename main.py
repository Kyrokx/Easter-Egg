import pygame

from src.Game import Game

print(" ============================================ ")
print(" By Kyrokx()#7573 🦊 ")
print(" ============================================ ")

# Initier le module pygame
pygame.init()

# Information de la fenêtre [
pygame.display.set_caption(" Easter Bunny ")
pygame.display.set_icon(pygame.image.load('assets/panier.png'))
screen = pygame.display.set_mode((800 , 480))
# ]

# Les images [
background = pygame.image.load('assets/fond.jpg')
ground = pygame.image.load('assets/sol.png')
# ]
run = True

game = Game()

# Boucle qui s'exetue [
while run:

    # Appliquer le fond
    screen.blit(background , (0 , 0))

    # Appliquer le sol
    screen.blit(ground , (0 , 0))

    # Appliquer l'image du player
    screen.blit(game.player.image , game.player.rect)

    # Mouvement du joueur
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
# ]
