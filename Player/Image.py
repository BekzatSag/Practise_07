import pygame

class Image:
    def __init__(self, screen, index_music, list_of_songs_images):
        self.screen = screen
        self.index_music = index_music
        self.list_of_songs_images = list_of_songs_images
    def draw(self, screen):
        self.image = pygame.image.load(self.list_of_songs_images[self.index_music])
        self.image_scale = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image_scale.get_rect(center = (500, 500))
        screen.blit(self.image_scale, self.rect)

