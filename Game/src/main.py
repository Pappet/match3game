import pygame
from pygame.locals import *

# Initialisierung von pygame
pygame.init()

# Konstanten definieren
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BACKGROUND_COLOR = (50, 50, 50)  # Grau

# Fenster erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Einfache Pygame Vorlage")

# Hauptspiel-Schleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()

pygame.quit()
