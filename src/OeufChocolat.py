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

    def repositionner(self):
        self.rect.x = random.randint(20, 800 - 40)
        self.rect.y = - self.image.get_height()
        self.vitesse_chute = random.randint(1, 3)

    def gravity(self):
        self.rect.y += self.velocity

        if pygame.sprite.spritecollide(self, self.player_group, False, pygame.sprite.collide_mask) and self.rect.y >= 360:
             print("Collision", self.rect.y)
             self.repositionner()