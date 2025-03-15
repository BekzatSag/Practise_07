import pygame
import sys
HEIGHT = 1000
WIDTH = 1000
WHITE = (255, 255, 255)
RED = (255, 0, 0)
initial_position = [HEIGHT//2, WIDTH//2]
speed = 20
radius = 25
pygame.init()

pygame.display.set_caption("Ball")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                if (initial_position[1]+speed <= HEIGHT-radius): initial_position[1]= (initial_position[1] + speed)

            if event.key==pygame.K_UP:
                if (initial_position[1]-speed >= 0+radius): initial_position[1]= (initial_position[1] - speed)

            if event.key==pygame.K_LEFT:
                if (initial_position[0]-speed >= 0+radius): initial_position[0]= (initial_position[0] - speed)

            if event.key==pygame.K_RIGHT:
                if (initial_position[0]+speed <= WIDTH-radius): initial_position[0]= (initial_position[0] + speed)

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, initial_position, radius)
    pygame.display.flip()
