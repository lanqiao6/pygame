import pygame


border_col = (0, 0, 0)
rect_col = (255, 255, 0)

x = 100
y = 100
w = 100
h = 100
border = 3


pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255,255,255))
    #draw border first
    #pygame.draw.rect(screen, border_col, (x, y, w, h))
    #then inside
    pygame.draw.rect(screen, rect_col, (x + border, y + border, w - border*2, h - border*2),50)

    pygame.display.update()

pygame.quit()
