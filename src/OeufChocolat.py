import pygame
import random


class OeufChocolat(pygame.sprite.Sprite):
    def __init__(self , width , heigth):
        super().__init__()
        self.image = pygame.image.load("assets/carrot.png")
        self.image = pygame.transform.scale(self.image , (40 , 40))
        self.velocity = random.randint(1 , 4)
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = heigth

    def remove(self):
        self.remove()

    def repositionner(self):
        # reteleporter l'oeuf en haut
        self.rect.x = random.randint(20, self.rect.x - 40)
        self.rect.y = - self.image.get_height()
        self.velocity = random.randint(1, 3)

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
