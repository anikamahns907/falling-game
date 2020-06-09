import pygame
import time
import random
 
pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 1200

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Anika's falling game")

game_over = False
 
x1 = 300
y1 = 300
 

 
clock = pygame.time.Clock()
 


anikaImg = pygame.image.load('anika.PNG').convert_alpha()


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = anikaImg
        self.rect = self.image.get_rect(center=pos)

player1 = Player((100, 300))


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1 > 5:
                x1 = x1 - 1
            elif event.key == pygame.K_RIGHT and x1 < dis_width - 5:
                x1 = x1 + 1
            elif event.key == pygame.K_UP and y1 <dis_height - 5:
                y1 = y1 - 1
            elif event.key == pygame.K_DOWN and y1 > 5:
                y1 = y1 + 1

 

    dis.fill(blue)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    dis.blit(player1.image, player1.rect)
    pygame.display.update()
 
    clock.tick(30)
 
pygame.quit()
quit()
