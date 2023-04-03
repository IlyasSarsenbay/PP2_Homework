import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30


clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y>47: y -= 20
        if pressed[pygame.K_DOWN] and y<251: y += 20
        if pressed[pygame.K_LEFT] and x>30: x -= 20
        if pressed[pygame.K_RIGHT] and x<351: x += 20
        
        screen.fill((255, 255, 255))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.circle(screen, (255,0,0), (x,y), 25)
        
        pygame.display.flip()
        clock.tick(60)