import pygame


# Classe du joueur "Panier"
class Panier(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Information du Sprite
        self.velocity = 3
        self.image = pygame.image.load('assets\panier.png')  # Image de dépard
        self.image = pygame.transform.scale(self.image , (120 , 120))  # Image rétréci
        self.rect = self.image.get_rect()
        self.rect.x = 285
        self.rect.y = 285

    # Bouger a droite
    def move_right(self):
        self.rect.x += self.velocity

    # Bouger a gauche
    def move_left(self):
        self.rect.x -= self.velocity