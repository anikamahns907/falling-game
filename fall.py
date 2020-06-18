import pygame
import time
import random

#start pygame
pygame.init()

#setting colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#setting width and height variable
dis_width = 600
dis_height = 900

#Sets width and height, initializes display into variable dis
dis = pygame.display.set_mode((dis_width, dis_height))

#Puts file name in corner
pygame.display.set_caption("Anika's falling game")

#Starting coords
x1 = 300
y1 = 300

#loading picture into variable
anikaImg = pygame.image.load('anika.PNG').convert_alpha()

#Set Player class
class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = anikaImg
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


#creates anika sprite
anika = Player([x1, y1])
#initializes pygame clock and saves it to a variable
clock = pygame.time.Clock()

#sets game over variable for following loop
game_over = False

while not game_over:
    dis.fill(blue)
    #sets sprite onto screen
    dis.blit(anika.image, anika.rect)
    
    
    #setting quit function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x1 > 0:
        x1 -= 2
    if keys[pygame.K_RIGHT] and x1 < dis_width - 163:
        x1 += 2
    if keys[pygame.K_UP] and y1 > 0:
        y1 -= 2
    if keys[pygame.K_DOWN] and y1 < dis_height - 193:
        y1 += 2
    anika.rect.topleft = [x1, y1]
    # we update the screen at every frame
    pygame.display.update()
    #sets frames per minute
    clock.tick(120)
 
pygame.quit()
quit()
#pygame.display.update()