import pygame

from src.Panier import Panier

from src.game import Game

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

# Boucle qui s'exetue [
while run:



    # Appeler le Player
    player = Panier()
    game = Game()

    # Appliquer le fond
    screen.blit(background , (0 , 0))
    # Appliquer le sol
    screen.blit(ground , (0 , 0))
    # Appliquer l'image du player
    screen.blit(player.image , player.rect)

    # Ajouter le Sprite Panier
    player_Sprite = pygame.sprite.Group()
    player_Sprite.add(player)

    if game.pressed.get(pygame.K_RIGHT):
        player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        player.move_left()
    # Mettre a jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        import time

        # l'evenement est la fermeture de la fenetre
        if event.type == pygame.QUIT:
            time.sleep(1)
            run = False
            pygame.quit()
            print(" ⏳ ... Entrain de se fermer !... ")

            time.sleep(2)
            print(" ❌ Fermeture de la fenêtre PyGame ! ")


        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
    # print(game.pressed)
# ]
