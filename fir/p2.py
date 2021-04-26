
import pygame
import sys

# pygame.init()

space = 60  # 四周留下的边距
cell_size = 40  # 每个格子的大小
cell_num = 15

grid_size = cell_size * (cell_num - 1) + space * 2  # 棋盘大小

screen = pygame.display.set_mode((grid_size, grid_size))

chess_arr = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            xi = round((x-space)/cell_size)
            yi = round((y-space)/cell_size)
            
            if xi >= 0 and xi < cell_num and yi >= 0 and yi < cell_num and (xi,yi) not in chess_arr:
                chess_arr.append((xi, yi))
  
    screen.fill((0, 0, 150))

    for x in range(0, cell_size*cell_num, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (x+space, 0+space),
                         (x+space, cell_size*(cell_num-1)+space), 1)
    for y in range(0, cell_size*cell_num, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (0+space, y+space),
                         (cell_size*(cell_num-1)+space, y+space), 1)

    for x, y in chess_arr:
        pygame.draw.circle(screen, (200, 200, 200),
                           (x*cell_size+space, y*cell_size+space), 16, 16)

    pygame.display.update()

pygame.quit()
