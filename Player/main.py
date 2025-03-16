import pygame
import sys
from Buttons import Button
from Image import Image
HEIGHT = 1000
WIDTH = 1000
DARK_GREY = (34, 34, 34)
GREY = (138, 128, 128)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test player")


class songs_text:
    def __init__(self, text):
        self.text = text
    def draw(self):
        self.text_song = pygame.font.Font(None, 40)
        self.text_song_render = self.text_song.render(self.text, True, WHITE)
        self.text_rect = self.text_song_render.get_rect(center = (500, 775))
        screen.blit(self.text_song_render, self.text_rect)

list_of_songs = ["Images and songs\Imagine Dragons - Dream.mp3", "Images and songs\Valentin Strukalo - Ulitsa Stalevarov.mp3", "Images and songs\Cyberpunk - Edgerunners.mp3","Images and songs\Death - Spirit Crusher.mp3"]
list_of_songs_names = ["Imagine Dragons — Dream", "Valentin Strukalo — Ulitsa Stalevarov", "Cyberpunk — Edgerunners","Death — Spirit Crusher"]
index_track = 0

user_event = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(user_event)
pygame.mixer.music.load(list_of_songs[index_track])
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()
UNPAUSE = True

list_of_songs_images = ["Images and songs\Imagine Dragons.png", "Images and songs\Valentin Strukalo.jpg", "Images and songs\Cyberpunk.jpg", "Images and songs\Death.png"]
image = Image(screen, index_track, list_of_songs_images)


pause_unpause = Button(WIDTH//2 - WIDTH//5//2, HEIGHT - HEIGHT//5, WIDTH//5, HEIGHT//10, "PAUSE", 20)
next = Button(WIDTH//2 - WIDTH//5//2 + WIDTH//4, HEIGHT - HEIGHT//5, WIDTH//10, HEIGHT//10, "->", 50)
previous = Button(WIDTH//2 - WIDTH//5//2 - (WIDTH//2 - WIDTH//5//2 + WIDTH//4 - (WIDTH//2 - WIDTH//5//2 + WIDTH//5) + WIDTH//10) , HEIGHT - HEIGHT//5, WIDTH//10, HEIGHT//10, "<-", 50)
songs_names = songs_text(list_of_songs_names[index_track])

running = True
while running: 
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()

        if event.type == user_event:
            index_track = (index_track+1)%len(list_of_songs)
            image.index_music = index_track
            pygame.mixer.music.load(list_of_songs[index_track])
            pygame.mixer.music.play() 


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if UNPAUSE:
                    pause_unpause.text = "UNPAUSE"
                    pygame.mixer.music.pause()
                else: 
                    pause_unpause.text ="PAUSE"
                    pygame.mixer.music.unpause()
                UNPAUSE = not UNPAUSE

            if event.key == pygame.K_RIGHT:
                index_track = (index_track+1)%len(list_of_songs)
                image.index_music = index_track
                UNPAUSE  = True
                pause_unpause.text ="PAUSE"
                image.index_music = index_track
                
                pygame.mixer.music.load(list_of_songs[index_track])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT:
                index_track = (index_track-1)%len(list_of_songs)
                image.index_music = index_track
                UNPAUSE  = True
                pause_unpause.text ="PAUSE"
                pygame.mixer.music.load(list_of_songs[index_track])
                pygame.mixer.music.play()


        if pause_unpause.is_clicked(event):
            if UNPAUSE:
                pause_unpause.text = "UNPAUSE"
                pygame.mixer.music.pause()
            else:
                pause_unpause.text ="PAUSE"
                pygame.mixer.music.unpause()
            UNPAUSE = not UNPAUSE

        if next.is_clicked(event):
            index_track = (index_track+1)%len(list_of_songs)
            image.index_music = index_track
            UNPAUSE  = True
            pause_unpause.text ="PAUSE"
            pygame.mixer.music.load(list_of_songs[index_track])
            pygame.mixer.music.play()

        if previous.is_clicked(event):
            index_track = (index_track-1)%len(list_of_songs)
            image.index_music = index_track
            UNPAUSE  = True
            pause_unpause.text ="PAUSE"
            pygame.mixer.music.load(list_of_songs[index_track])
            pygame.mixer.music.play()


    screen.fill(DARK_GREY)
    pause_unpause.draw(screen)
    next.draw(screen)
    previous.draw(screen)
    image.draw(screen)
    songs_names.text = list_of_songs_names[index_track]
    songs_names.draw()
    pygame.display.flip()
    
