from calendar_ex import clean
import pygame

pygame.init()

space = 60
cell_num = 15
cell_size = 40
grid_size = cell_size * (cell_num - 1) + space * 2

screen = pygame.display.set_mode((grid_size,grid_size))


is_exit = False
while not is_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_exit = True
    screen.fill((0,0,150))

    for x in range(0,15):
        pygame.draw.line(screen,(255,255,255),(space+ x * cell_size,space),(space+ x * cell_size , (grid_size - space)),1)
    for y in range(0,15):
        pygame.draw.line(screen,(255,255,255),(space,(space + y * cell_size)),((grid_size-space),(space+ y * cell_size)),1)
    
    pygame.display.flip()

pygame.quit()




