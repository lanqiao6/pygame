
import pygame

#pygame必须的初始化工作
pygame.init()

space = 60  # 四周留下的边距
cell_size = 40  # 每个格子的大小
cell_num = 15
grid_size = cell_size * (cell_num - 1) + space * 2  # 棋盘大小

#创建一个图形化用户界面（窗口）。坐标系统。像素。
screen = pygame.display.set_mode((grid_size, grid_size))

chess_arr = []
flag = 1  # 1为黑色，2为白色
game_state = 1 # 游戏状态1.表示正常进行 2.表示黑胜 3.表示白胜

def get_one_dire_num(lx, ly, dx, dy, m):
    tx = lx
    ty = ly
    s = 0
    while True:
        tx += dx
        ty += dy
        if tx < 0 or tx >= cell_num or ty < 0 or ty >= cell_num or m[ty][tx] == 0: return s
        s+=1

def check_win(chess_arr, flag):
    m = [[0]*cell_num for i in range(cell_num)] # 先定义一个15*15的全0的数组,不能用[[0]*cell_num]*cell_num的方式去定义因为一位数组会被重复引用
    for x, y, c in chess_arr:
        if c == flag:
            m[y][x] = 1 # 上面有棋则标1
    lx = chess_arr[-1][0] # 最后一个子的x
    ly = chess_arr[-1][1] # 最后一个子的y
    dire_arr = [[(-1,0),(1,0)],[(0,-1),(0,1)],[(-1,-1),(1,1)],[(-1,1),(1,-1)]] # 4个方向数组,往左＋往右、往上＋往下、往左上＋往右下、往左下＋往右上，4组判断方向
    
    for dire1,dire2 in dire_arr:
        dx, dy = dire1
        num1 = get_one_dire_num(lx, ly, dx, dy, m)
        dx, dy = dire2
        num2 = get_one_dire_num(lx, ly, dx, dy, m)
        if num1 + num2 + 1 >= 5: return True

    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if game_state == 1 and event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            xi = round((x-space)/cell_size)
            yi = round((y-space)/cell_size)
            if xi >= 0 and xi < cell_num and yi >= 0 and yi < cell_num and (xi, yi, 1) not in chess_arr and (xi, yi, 2) not in chess_arr:
                chess_arr.append((xi, yi, flag))
                if check_win(chess_arr,flag):
                    game_state = 2 if flag == 1 else 3
                else:
                    flag = 2 if flag == 1 else 1

    screen.fill((0, 0, 150))

    for x in range(0, cell_size*cell_num, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (x+space, 0+space),
                         (x+space, cell_size*(cell_num-1)+space), 1)
    for y in range(0, cell_size*cell_num, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (0+space, y+space),
                         (cell_size*(cell_num-1)+space, y+space), 1)

    for x, y, f in chess_arr:
        chess_color = (30, 30, 30) if f == 1 else (200, 200, 200)
        pygame.draw.circle(screen, chess_color,
                           (x*cell_size+space, y*cell_size+space), 16, 16)

    if game_state != 1:

        #使用系统的默认字体，字体大小为60个点，
        myfont = pygame.font.Font(None,60)
        win_text = "%s win"%('black' if game_state == 2 else 'white')
        textImage = myfont.render(win_text,True,(210,210,0))
        screen.blit(textImage,(260,320))

    pygame.display.update()

pygame.quit()
