import pygame
from tkinter import *
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


#code for drawing line
def drawLineBetween(screen, index, start, end, width, color_mode):
    #changing brightness of color
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))  
    #setting colors
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    #Eraser
    elif color_mode == 'black':
        color = (0,0,0)
    #coordinates of line
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)    

radius = 15
x = 0
y = 0
mode = 'blue'
points = []
color = (255,0,0)
while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    exit()
                if event.key == pygame.K_F4 and alt_held:
                    exit()
                if event.key == pygame.K_ESCAPE:
                    exit()
                # determine if a letter key was pressed and changing colors
                if event.key == pygame.K_r:
                    mode = 'red'
                    color=(255,0,0)
                elif event.key == pygame.K_g:
                    mode = 'green'
                    color=(0,255,0)
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    color=(0,0,255)
                elif event.key == pygame.K_e:
                    mode = 'black'
                    i=20
                   
                    #draw a rectangle
                if event.key == pygame.K_v:
                    pygame.draw.rect(screen,color,(100,200,150,100))
                    #draw a circle
                if event.key == pygame.K_c:
                     pygame.draw.circle(screen, color, (600,50), 25)
                 #draw a square
                if event.key == pygame.K_s:
                    pygame.draw.rect(screen,color,(20,350,100,100))
                    #draw a right triangle
                if event.key == pygame.K_t:
                    pygame.draw.lines(screen,color,True,[[600, 400], [500, 400], [500, 300]])
                    #draw a equileteral triangle
                if event.key == pygame.K_y:
                    pygame.draw.lines(screen,color,True,[[0, 0], [50, 50*3*0.5], [100, 0]])
                    #draw a rhombus
                if event.key == pygame.K_f:
                    pygame.draw.polygon(screen,color,[[450,300],[600,200],[450,100],[300,200]])
                   
                  

                
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
            
                
            
              
        
        
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)