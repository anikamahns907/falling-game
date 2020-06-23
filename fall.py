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


item_height = 20

#Sets width and height, initializes display into variable dis
dis = pygame.display.set_mode((dis_width, dis_height))

#Puts file name in corner
pygame.display.set_caption("Anika's falling game")

img_height = 193
img_width = 163
#Starting coords
x1 = (dis_width/2) - (img_width/2)
y1 = dis_height-img_height


pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)



#loading picture into variable
anikaImg = pygame.image.load('anika.PNG').convert_alpha()

#Set Player class
class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = anikaImg
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    def restart(self):
        x1 = (dis_width/2) - (img_width/2)
        y1 = dis_height-img_height  
        self.rect.topleft = [x1, y1]

endScreen = pygame.image.load('gameoverscreen.png').convert_alpha()
pooImg = pygame.image.load('po.jpeg').convert_alpha()
anonImg = pygame.image.load('anon.png').convert_alpha()
satImg = pygame.image.load('sat.jpg').convert_alpha()

anika = Player([x1, y1])
#Set fallItem class
class fallItem(pygame.sprite.Sprite):
    
    def __init__(self, isGood, imageType, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = imageType
        self.good = isGood
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self):
        self.rect.y += 2
        if self.rect.y > dis_height:
            self.rect.topleft= [random.randint(0,dis_width), 0 - item_height]
    def restart(self):
        self.rect.topleft= [random.randint(0,dis_width), 0 - item_height]

    def is_collided_with(self, anika):
        
        return self.rect.colliderect(anika.rect)
#creates anika sprite
pooItem = fallItem(False, pooImg, [random.randint(0,dis_width), 0 - item_height])
anonItem = fallItem(True, anonImg, [random.randint(0,dis_width), 0 - item_height])
satItem = fallItem(True, satImg, [random.randint(0,dis_width), 0 - item_height])
#all_sprites.add(pooItem)
#initializes pygame clock and saves it to a variable
clock = pygame.time.Clock()

#sets game over variable for following loop
game_over = False
game_open = True
end_screen = True

while game_open:
    print("starting game")
    score = 0
    while not game_over:
        textsurface = myfont.render('Score: ' + str(score), False, (0, 0, 0))
        dis.fill(blue)
        #sets sprite onto screen
        dis.blit(anika.image, anika.rect)
        dis.blit(pooItem.image, pooItem.rect)
        dis.blit(anonItem.image, anonItem.rect)
        dis.blit(satItem.image, satItem.rect)
        dis.blit(textsurface,(0,0))

        #setting quit function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_open = False
                game_over = True
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x1 > 0:
            x1 -= 2
        if keys[pygame.K_RIGHT] and x1 < dis_width - img_width:
            x1 += 2

        if anonItem.is_collided_with(anika):
            anonItem.restart()
            score = score + 1

        if satItem.is_collided_with(anika):
            satItem.restart()
            score = score + 2

        if pooItem.is_collided_with(anika):
            anika.restart()
            pooItem.restart()
            end_screen = True
            game_over = True
            
        # if keys[pygame.K_UP] and y1 > 0:
        #     y1 -= 2
        # if keys[pygame.K_DOWN] and y1 < dis_height - img_height:
        #     y1 += 2
        anika.rect.topleft = [x1, y1]
        # we update the screen at every frame
        pooItem.update()
        anonItem.update()
        satItem.update()
        pygame.display.update()
    

        #all_sprites.draw(dis)
        clock.tick(120)
    dis.blit(endScreen, (0, 0))
    pygame.display.update()
    #Show the game over screen
    while end_screen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    print("exit")
                    game_open = False
                    end_screen = False
                    print("exit")
                    break
                if event.key == pygame.K_SPACE:
                    print("restart")
                    game_over = False
                    end_screen = False
                    print("restart")
                    break
        clock.tick(120)

 

pygame.quit()
quit()
#pygame.display.update()




