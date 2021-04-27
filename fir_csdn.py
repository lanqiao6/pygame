
import pygame
import sys

pygame.init()

cell_num = 15
cell_size = 40
space = 60

grid_size = (cell_num-1) * cell_size + space*2
screen = pygame.display.set_mode((grid_size, grid_size))

chess_arr = []  # 存储棋盘中的棋子
flag = 1  # 1为黑色,2为白色
game_state = 1  # 1正常，2黑胜，3白胜


def get_one_dire_num(dire, lx, ly, m):
    '''计算一个方向上面连续的棋子'''
    tx = lx
    ty = ly
    dx, dy = dire
    s = 0
    while True:
        tx += dx
        ty += dy
        if tx < 0 or tx >= cell_num or ty < 0 or ty >= cell_num or m[tx][ty] == 0:
            return s
        s += 1


def check_win(chess_arr, flag):
    m = [[0]*cell_num for i in range(cell_num)]
    for x, y, f in chess_arr:
        if f == flag:
            m[x][y] = 1
    lx = chess_arr[-1][0]
    ly = chess_arr[-1][1]
    dire = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)],
            [(1, 1), (-1, -1)], [(1, -1), (-1, 1)]]
    for dire1, dire2 in dire:
        num1 = get_one_dire_num(dire1, lx, ly, m)
        num2 = get_one_dire_num(dire2, lx, ly, m)
        if num1+num2+1 == 5:
            return True
    return False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_state == 1 and event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            xi = round((x-space)/cell_size)
            yi = round((y-space)/cell_size)
            flag = 2 if flag == 1 else 1
            if xi >= 0 and xi < cell_num and yi >= 0 and yi < cell_num and (xi, yi, 1) not in chess_arr and (xi, yi, 2) not in chess_arr:
                chess_arr.append((xi, yi, flag))
            if check_win(chess_arr, flag):
                game_state = 2 if flag == 1 else 3

    screen.fill((0, 0, 150))

    for x in range(0, cell_num):
        pygame.draw.line(screen, (255, 255, 255), (x*cell_size +
                         space, space), (x*cell_size+space, grid_size-space), 1)
    for y in range(0, cell_num):
        pygame.draw.line(screen, (255, 255, 255), (space, y *
                         cell_size+space,), (grid_size-space, y*cell_size+space), 1)

    for xi, yi, c in chess_arr:
        chess_color = (200, 200, 200) if c == 2 else (0, 0, 0)
        pygame.draw.circle(screen, chess_color,
                           (xi*cell_size+space, yi*cell_size+space), 16, 16)

    if game_state != 1:
        myfont = pygame.font.Font(None, 100)
        text = "%s win" % ("black" if game_state == 2 else "white")
        textImage = myfont.render(text, True, (210, 210, 0))
        screen.blit(textImage, (180, 320))

    pygame.display.update()
