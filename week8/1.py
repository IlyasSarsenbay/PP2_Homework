import pygame, sys
from pygame.locals import *
import random, time

#Code for saving data about coins
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, score, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.score = score
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - 60:
            self.rect.y += self.speed
        else:
            self.kill()

#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
game_score = 0

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#loading images of background and coins
background = pygame.image.load("c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week8/AnimatedStreet.png")
balls_data = ({'path': 'coin1.png', 'score': 100},
              {'path': 'coin2.png', 'score': 150},
              {'path': 'coin3.png', 'score': 200})
balls_surf = [pygame.image.load(data['path']) for data in balls_data]
#group coins
balls = pygame.sprite.Group()

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
#Creating Enemy and Player sprites
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 #setting work of scoring points
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) 
   #setting buttons for moving     
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
#setting random position and speed of coins
def createBall(group):
    indx = random.randint(0, len(balls_surf)-1)
    x = random.randint(20, SCREEN_WIDTH-20)
    speed = random.randint(2, 4)

    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)


createBall(balls)
speed = 10
#Setting collision of coins and player's sprite
def collideBalls():
    global game_score
    for ball in balls:
        if pygame.sprite.spritecollideany(P1,balls):
            game_score += ball.score 
            ball.kill()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
pygame.time.set_timer(pygame.USEREVENT, 2000)
#Game Loop
while True:
       
    #Cycles through all events occurring  (closing game,incresing speed of enemy and creating coins)
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)
    #setting background image and scores on screen
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
        
    

    #"Game over" if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week8/crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()   
    #setting coins and score of getting coins on screen
    balls.draw(DISPLAYSURF)
    DISPLAYSURF_text = font_small.render(str(game_score), 1, BLACK)
    DISPLAYSURF.blit(DISPLAYSURF_text, (350, 10))
    pygame.display.update()
    FramePerSec.tick(FPS)
    #recreating coins
    balls.update(SCREEN_HEIGHT)
    collideBalls()