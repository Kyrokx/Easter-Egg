import pygame
import random


class OeufChocolat(pygame.sprite.Sprite):
    def __init__(self , width , heigth, player):
        super().__init__()
        self.player = player
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        ################################
        self.image = pygame.image.load("assets/carrot.png")
        self.image = pygame.transform.scale(self.image , (40 , 40))
        self.velocity = random.randint(1 , 4)
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = heigth

    def remove(self):
        self.remove()

    def gravity(self):
        self.rect.y += self.velocity

        if self.rect.y >= 300:
            pass
            # self.remove()

        # # verifier si la boule de jeu touche le joueur
        # if self.game.check_collision(
        #         self , self.game.player_Sprite
        # ):
        #     print(" 👊 Toucher ! ")
        #     # retirer la boule de feu
        #     self.remove()
