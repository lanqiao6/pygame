
import pygame
import sys

pygame.init()

cell_num = 15
cell_size = 40
space = 60

grid_size = (cell_num-1) * cell_size + space*2
screen = pygame.display.set_mode((grid_size,grid_size))

chess_arr = []  #存储棋盘中的棋子  
flag = 1    #1为黑色,2为白色

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            xi = round((x-space)/cell_size)
            yi = round((y-space)/cell_size)
            flag = 2 if flag == 1 else 1
            if xi>=0 and xi<cell_num and yi>=0 and yi<cell_num and (xi,yi,1) not in chess_arr and (xi,yi,2) not in chess_arr:   
                chess_arr.append((xi,yi,flag))

    screen.fill((0,0,150))

    for x in range(0,cell_num):
        pygame.draw.line(screen,(255,255,255),(x*cell_size+space,space),(x*cell_size+space,grid_size-space),1)
    for y in range(0,cell_num):
        pygame.draw.line(screen,(255,255,255),(space,y*cell_size+space,),(grid_size-space,y*cell_size+space),1)
    
    for xi,yi,c in chess_arr:
        chess_color = (200,200,200) if c == 2 else (0,0,0)
        pygame.draw.circle(screen,chess_color,(xi*cell_size+space,yi*cell_size+space),16,16)

    pygame.display.update()