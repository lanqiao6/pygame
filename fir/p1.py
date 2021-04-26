
import pygame

#pygame.init()

space = 60 #四周留下的边距
cell_size = 40 #每个格子的大小
cell_num = 15 

grid_size = cell_size * (cell_num - 1) + space * 2 #棋盘大小

screen = pygame.display.set_mode((grid_size,grid_size))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0,0,150))

    for x in range(0,cell_size*cell_num,cell_size):
        pygame.draw.line(screen,(200,200,200),(x+space,0+space),(x+space,cell_size*(cell_num-1)+space),1)
    for y in range(0,cell_size*cell_num,cell_size):
        pygame.draw.line(screen,(200,200,200),(0+space,y+space),(cell_size*(cell_num-1)+space,y+space),1)
        
    
    pygame.display.update()

pygame.quit()
