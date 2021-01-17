import pygame

from src.Panier import Panier


# Class Game
class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Appeler la Class Panier
        self.player = Panier()
        # Ajouter le Sprite Panier
        self.player_Sprite = pygame.sprite.Group()
        self.player_Sprite.add(self.player)
        
        self.pressed = {}
