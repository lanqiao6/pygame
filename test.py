
import pygame

cell_num = 15
cell_size = 40
space = 60

black = (0, 0, 0)
white = (255, 255, 255)

grid_size = cell_size * (cell_num - 1) + space * 2

screen = pygame.display.set_mode((grid_size, grid_size))

chess_arr = []
flag = 1

isExit = False

while not isExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isExit = True
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            xi = round((x-space)/cell_size)
            yi = round((y-space)/cell_size)
            if xi >= 0 and xi < cell_num and yi >= 0 and yi < cell_num and (xi, yi, 1) not in chess_arr and (xi, yi, 2) not in chess_arr:
                chess_arr.append((xi, yi, flag))
                flag = 2 if flag == 1 else 1
            print(chess_arr)

    screen.fill((0, 150, 200))

    for i in range(0, cell_num):
        pygame.draw.line(screen, black, (space, space+i*cell_size),
                         (grid_size-space, space+i*cell_size), 1)
    for j in range(0, cell_num):
        pygame.draw.line(screen, black, (space+j*cell_size, space),
                         (space+j*cell_size, grid_size-space), 1)

    for x, y, c in chess_arr:
        chess_color = black if c == 1 else white
        pygame.draw.circle(screen, chess_color,
                           (x*cell_size+space, y*cell_size+space), 16, 16)

    pygame.display.update()

pygame.quit()
