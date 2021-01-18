import pygame

from src.Panier import Panier

from src.OeufChocolat import OeufChocolat


# Class Game
class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Appeler la Class Panier
        self.player = Panier()
        # Appeler la class oeuf
        self.egg = OeufChocolat(0,0)
        self.eggs_sprite = pygame.sprite.Group()
        # Ajouter le Sprite Panier
        self.player_Sprite = pygame.sprite.Group()
        self.player_Sprite.add(self.player)
        self.pressed = {}

    def tg(self):
        self.spawn_egg()
        self.spawn_egg()
        self.spawn_egg()

    def check_collision(self , sprite , group):
        return pygame.sprite.spritecollide(sprite , group , False , pygame.sprite.collide_mask)

    def spawn_egg(self):
        self.eggs_sprite.add(self.egg)