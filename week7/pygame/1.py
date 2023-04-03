import pygame
pygame.init()
import datetime
W, H = 800, 800
x = W//2
y = H//2
d=75-6.1*int(datetime.datetime.now().strftime("%S"))
m=85-5.8*int(datetime.datetime.now().strftime("%M"))
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))

mickey = pygame.image.load("c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week7/pygame/main-clock.png")
leftHand = pygame.image.load("c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week7/pygame/left-hand.png")
rightHand = pygame.image.load("c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week7/pygame/right-hand.png")
mickeyRect = mickey.get_rect()
def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = center).center)
    surf.blit(rotated_image, new_rect)
langle = 0
rangle = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    langle -= 0.006872
    rangle -= 0.412
    
    sc.fill(WHITE)
    sc.blit(mickey, (x, y))
    sc.blit(mickey, mickeyRect)
    blitRotateCenter(sc, leftHand, (x,y), m+langle) 
    blitRotateCenter(sc, rightHand, (x,y),d+rangle)
    pygame.display.update()

    #75 - righthand and 85 - lefthand
