import pygame
import time
import random

# Time variables and Lists of the files
shortClock = random.randrange(1, 2)
noise = ['Auxiliary.wav', 'Bed.wav', 'Blinds.wav', 'Bounce.wav', 'Box.wav', 'Candle.wav', 'Door Shut.wav',
         'Ethernet.wav', 'Hangers.wav', 'Humidifier.wav', 'Keys.wav', 'Knock.wav', 'Light Switch.wav',
         'LightSwitch2.wav', 'Lock.wav', 'Mouse.wav', 'Pew.wav', 'Piano.wav', 'Pillow.wav', 'Radio.wav',
         'Remotedrop.wav', 'RollerChair.wav', 'Sink.wav', 'Tv.wav', 'Typing.wav', 'WaterBottle.wav']
picture = ['Auxiliary.jpg', 'Bed.jpg', 'Blinds.jpg', 'Bounce.jpg', 'Box.jpg', 'Candle.jpg', 'Door Shut.jpg',
           'Ethernet.jpg', 'Hangers.jpg', 'Humidifier.jpg', 'Keys.jpg', 'Knock.jpg', 'Light Switch.jpg',
           'LightSwitch2.jpg', 'Lock.jpg', 'Mouse.jpg', 'Pew.jpg', 'Piano.jpg', 'Pillow.jpg', 'Radio.jpg',
           'Remotedrop.jpg', 'RollerChair.jpg', 'Sink.jpg', 'Tv.jpg', 'Typing.jpg', 'WaterBottle.jpg']

# Initialize mixer and display. Sounds will play over one another
pygame.init()
pygame.mixer.init()
# Setting up a window
window_width = 1400
window_height = 800
gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('A Soundscape Portrait of my Room')


def update():
    # Infinite loop of playing sounds
    while True:
        # If the close button is clicked the program ends
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # Choose a random sound from the noise list
        r_num = random.randrange(0, len(noise))
        rand_noise = pygame.mixer.Sound(noise[r_num])

        # After choosing the picture and song, these lines set the picture to be displayed
        current_picture = pygame.image.load(picture[r_num])
        scaled_picture = pygame.transform.scale(current_picture, (1400, 800))
        gameDisplay.blit(scaled_picture, (0, 0))
        pygame.display.flip()

        # Plays sound and wait to play a new one
        rand_noise.play()
        time.sleep(shortClock)

# Calling the function
update()
