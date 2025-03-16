import pygame
HEIGHT_PAUSE_UNPAUSE = 100
WIDTH_PAUSE_UNPAUSE = 100
HEIGHT_PREVIOUS = 50
WIDTH_PREVIOUS = 50
HEIGHT_NEXT = 50
WIDTH_NEXT = 50
PURPLE = (102, 0, 204)
BLACK = (0, 0, 0)
GREY = (138, 128, 128)

class Button:
    def __init__(self, x, y, WIDTH, HEIGHT, text, font):
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.text = text
        self.font = pygame.font.Font(None, font)


    def draw(self, screen):
        pygame.draw.rect(screen, GREY, self.rect, border_radius = 5)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface, text_rect)


    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)