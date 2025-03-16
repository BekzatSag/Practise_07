import pygame 
import sys
import datetime
HEIGHT = 1000
WIDTH = 1000
center = (WIDTH//2, HEIGHT//2)
WITHE = (255, 255, 255)
ERROR_MINUTE_ANGLE = 54
ERROR_SECOND_ANGLE = -59
pygame.init()

pygame.mixer.music.load("clock.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")


clock = pygame.time.Clock()

image_clock = pygame.image.load("clock.jpg")
image_clock_rect = image_clock.get_rect(center = (WIDTH//2, HEIGHT//2))
angle = datetime.datetime.now().second * 6
end_x = center [0] + 100 * pygame.math.Vector2(0, -1).rotate(angle).x
end_y = center [1] + 100 * pygame.math.Vector2(0, -1).rotate(angle).y

minute_arrow_original = pygame.image.load("min_hand.png")
minute_arrow = minute_arrow_original 

second_arrow_original = pygame.image.load("sec_hand.png")
second_arrow = second_arrow_original 



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    now = datetime.datetime.now()
    second = now.second
    angle_second = -second * 6 - ERROR_SECOND_ANGLE

    minute = now.minute
    angle_minute = -6 * minute - ERROR_MINUTE_ANGLE

    second_arrow = pygame.transform.rotate(second_arrow_original, angle_second)    
    second_arrow_rect = second_arrow.get_rect(center = (WIDTH//2, HEIGHT//2))
    minute_arrow = pygame.transform.rotate(minute_arrow_original, angle_minute)
    minute_arrow_rect = minute_arrow.get_rect(center = (WIDTH//2, HEIGHT//2))

    screen.fill(WITHE)
    screen.blit(image_clock, image_clock_rect)
    screen.blit(second_arrow, second_arrow_rect)
    screen.blit(minute_arrow, minute_arrow_rect)
    
    pygame.display.flip()

