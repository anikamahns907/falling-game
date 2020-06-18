import pygame
#image is saved as a variable
anikaImg = pygame.image.load('anika.PNG').convert_alpha() 

class Anika(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, pos):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = anikaImg
        self.rect = self.image.get_rect(center=pos)




