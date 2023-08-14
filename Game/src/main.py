import pygame
from pygame.locals import *
import utilities

# Initialisierung von pygame
pygame.init()

# SETTINGS
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FULLSCREEN = False
FPS = 30
TITLE = "Match-3 Game"
BACKGROUND_COLOR = utilities.DarkGray

clock = pygame.time.Clock()

# Fenster erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
window_position = screen.get_rect().center
pygame.display.window_pos = window_position

# Hauptspiel-Schleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    pygame.display.update()
    # limit the frame rate to 60 FPS
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
quit()
