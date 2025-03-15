import pygame
import sys
from Buttons import Button
from Image import Image
HEIGHT = 1000
WIDTH = 1000
DARK_GREY = (34, 34, 34)
GREY = (138, 128, 128)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test player")



list_of_songs = ["Images and songs\Imagine Dragons - 09. Dream.mp3", "Images and songs\Valentin Strukalo.mp3", "Images and songs\Cyberpunk.mp3","Images and songs\Death - Spirit Crusher.mp3"]
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
    pygame.display.flip()
    
