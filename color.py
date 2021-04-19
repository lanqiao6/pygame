import pygame
import sys

pygame.init()
size = width, height = 320, 240
screen = pygame.display.set_mode(size)

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
colors = (BLACK, WHITE, RED, GREEN, BLUE)
n = 0
color = colors[n]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if n >= len(colors)-1:
                    n = 0
                else:
                    n += 1
                color = colors[n]

    screen.fill(color)
    pygame.display.flip()

pygame.quit()
