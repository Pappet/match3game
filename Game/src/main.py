import pygame
from pygame.locals import *
import utilities
import random


# Initialisierung von pygame
pygame.init()

# SETTINGS
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FULLSCREEN = False
FPS = 60
TITLE = "Match-3 Game"
BACKGROUND_COLOR = utilities.DarkGray

clock = pygame.time.Clock()

CELL_SIZE = 64
GRID_SIZE = 10

# Fenster erstellen
screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
pygame.display.set_caption(TITLE)
window_position = screen.get_rect().center
pygame.display.window_pos = window_position

# load images
images = [pygame.transform.scale(pygame.image.load(
    f'/home/peter/Projekte/match3game/Game/assets/images/image{i+1}.png').convert_alpha(), (CELL_SIZE, CELL_SIZE)) for i in range(5)]
blank_image = pygame.transform.scale(pygame.image.load(
    '/home/peter/Projekte/match3game/Game/assets/images/blank.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))


# Zufällige Auswahl der Bilder für das gesamte Raster VOR der Hauptspiel-Schleife
grid = [[random.choice(images) for _ in range(GRID_SIZE)]
        for _ in range(GRID_SIZE)]

# Hauptspiel-Schleife
running = True
selected_cell = None

# Funktion, um zu überprüfen, ob zwei Zellen Nachbarn sind (nur vertikal oder horizontal)


def are_neighbors(cell1, cell2):
    row1, col1 = cell1
    row2, col2 = cell2

    return (abs(row1 - row2) == 1 and col1 == col2) or (abs(col1 - col2) == 1 and row1 == row2)


def find_matches(grid):
    matches = []

    # Überprüfe horizontale Übereinstimmungen
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE - 2):  # -2, um einen Indexfehler zu vermeiden
            if grid[row][col] == grid[row][col + 1] == grid[row][col + 2]:
                matches.append([(row, col), (row, col + 1), (row, col + 2)])

    # Überprüfe vertikale Übereinstimmungen
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE - 2):  # -2, um einen Indexfehler zu vermeiden
            if grid[row][col] == grid[row + 1][col] == grid[row + 2][col]:
                matches.append([(row, col), (row + 1, col), (row + 2, col)])

    return matches


def drop_and_fill(grid, screen):
    moved = True
    while moved:
        moved = False  # Gehe davon aus, dass in dieser Runde nichts bewegt wird, bis das Gegenteil bewiesen ist
        for col in range(GRID_SIZE):
            # Starte von unten und gehe nach oben, aber ignoriere die oberste Zeile
            for row in range(GRID_SIZE - 1, 0, -1):
                # Wenn die aktuelle Zelle leer ist und die darüber ein Bild hat
                if grid[row][col] == blank_image and grid[row - 1][col] != blank_image:
                    grid[row][col], grid[row - 1][col] = grid[row -
                                                              1][col], blank_image  # Tausche die beiden Zellen
                    moved = True  # Ein Bild wurde in dieser Runde bewegt

                    # Zeichne das Raster erneut und aktualisiere den Bildschirm
                    screen.fill(BACKGROUND_COLOR)
                    for r in range(GRID_SIZE):
                        for c in range(GRID_SIZE):
                            screen.blit(
                                grid[r][c], (c * CELL_SIZE, r * CELL_SIZE))
                    pygame.display.flip()

                    # Warte eine kurze Zeit, um den Fall sichtbar zu machen (z.B. 50 Millisekunden)
                    pygame.time.wait(50)

        # Wenn alle fallenden Bilder den Boden erreicht haben, fülle die leeren Zellen am oberen Rand mit neuen Bildern
        for col in range(GRID_SIZE):
            if grid[0][col] == blank_image:
                grid[0][col] = random.choice(images)


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Position des Mausklicks ermitteln
            x, y = pygame.mouse.get_pos()

            # Bestimme die Zelle des Rasters, auf die geklickt wurde
            col = x // CELL_SIZE
            row = y // CELL_SIZE

            if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:
                if selected_cell:  # Wenn bereits eine Zelle ausgewählt wurde
                    if are_neighbors(selected_cell, (row, col)):
                        # Tausche die Bilder der beiden Zellen
                        grid[selected_cell[0]][selected_cell[1]
                                               ], grid[row][col] = grid[row][col], grid[selected_cell[0]][selected_cell[1]]
                    # Entferne die Auswahl
                    selected_cell = None
                else:
                    # Wähle die aktuelle Zelle aus
                    selected_cell = (row, col)

    screen.fill(BACKGROUND_COLOR)

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            screen.blit(grid[r][c], (c * CELL_SIZE, r * CELL_SIZE))

            if selected_cell == (r, c):
                pygame.draw.rect(
                    screen, (255, 0, 0), (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

    # ... (nachdem die Bilder getauscht wurden)
    matches = find_matches(grid)
    if matches:
        for match in matches:
            # Hier kannst du entsprechende Aktionen für jedes gefundene Match ausführen
            # Zum Beispiel:
            for cell in match:
                row, col = cell
                # Setzt die übereinstimmende Zelle auf None oder was auch immer du möchtest
                grid[row][col] = blank_image
        drop_and_fill(grid, screen)

    pygame.display.update()
    # limit the frame rate to 60 FPS
    clock.tick(FPS)

pygame.quit()
quit()
