
import pygame

pygame.init()

cell_num = 15
cell_size = 40
space = 60
grid_size = (cell_num-1)*40+space*2  
white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode((grid_size,grid_size))

flag = 1
chess_arr=[]
game_state = 1 

def get_one_dire_num(m,lx,ly,dire):
    n = 0
    tx = lx
    ty = ly
    dx,dy = dire
    while True:
        tx += dx
        ty += dy
        if tx<0 or tx>=cell_num or ty<0 or ty>=cell_num or  m[tx][ty] == 0:
            return n
        n+=1

def check_win(chess_arr,flag):
    m = [[0]*cell_num for i in range(cell_num)]
    for x,y,c in chess_arr:
        if c == flag :
            m[x][y] =1
    dire = [[(0,-1),(0,1)],[(-1,0),(1,0)],[(1,1),(-1,-1)],[(1,-1),(-1,1)]]
    lx = chess_arr[-1][0]
    ly = chess_arr[-1][1]
    for dir1,dir2 in dire:
        n1 = get_one_dire_num(m,lx,ly,dir1)
        n2 = get_one_dire_num(m,lx,ly,dir2)
        n = n1 + n2 + 1
        if n >= 5:
            return True

isExit = False
while not isExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isExit = True
        if event.type == pygame.MOUSEBUTTONUP and game_state == 1:
            x,y=pygame.mouse.get_pos()
            xi = round((x-space)/cell_size)
            yi = round((y-space)/cell_size)
            if  xi>=0 and xi<cell_num and yi>=0 and yi<cell_num and ((xi,yi,2) not in chess_arr) and ((xi,yi,1) not in chess_arr):
                chess_arr.append((xi,yi,flag))
                if check_win(chess_arr,flag):
                    game_state = 2 if flag == 1 else 3
                else:
                    flag = 2 if flag == 1 else 1
    
 
    screen.fill((0,150,200))

    for x in range(cell_num):
        pygame.draw.line(screen,black,(space,space+x*cell_size),(grid_size-space,space+x*cell_size),1)
    for y in range(cell_num):
        pygame.draw.line(screen,black,(space+y*cell_size,space),(space+y*cell_size,grid_size-space),1)

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT]:
        chess_arr=[]
        game_state = 1
        flag = 1

    for xi,yi,c in chess_arr:
        cell_color = black if c == 1 else white
        pygame.draw.circle(screen,cell_color,(xi*cell_size+space,yi*cell_size+space),16,16)
    
    if game_state != 1:
        myfont = pygame.font.Font(None,100)
        text = "%s win" % ("black" if game_state == 2 else "white")
        text_image = myfont.render(text,True,(210,210,210))
        screen.blit(text_image,(150,300))
    
    pygame.display.update()
    
pygame.quit()


    