
import pygame

pygame.init()

cell_num = 15
cell_size = 40
space = 60
grid_size = cell_size*(cell_num-1)+space*2

black = (0,0,0)
white = (255,255,255)

screen = pygame.display.set_mode((grid_size,grid_size))

chess_arr = []
flag = 1 #黑棋为1，白棋为2
game_state = 1 #正常进行时状态为1，黑棋胜为2，白棋胜为3

def get_one_dire_num(m,lx,ly,dire):
    n = 0    
    tx = lx
    ty = ly
    dx,dy = dire
    while True:
        tx += dx
        ty += dy
        if tx<0 or tx>=cell_num or ty<0 or ty>=cell_num or m[tx][ty] == 0:
            return n
        n+=1

def check_win(chess_arr,flag):
    m = [[0]*cell_num for i in range(0,cell_num)]
    for i,j,c in chess_arr:
        if c == flag:
            m[i][j] = 1
    lx = chess_arr[-1][0]
    ly = chess_arr[-1][1]  
    dire = [[(-1,0),(1,0)],[(0,1),(0,-1)],[(1,-1),(-1,1)],[(1,1),(-1,-1)]]
    for dir0,dir1 in dire: 
        n1 = get_one_dire_num(m,lx,ly,dir0)
        n2 = get_one_dire_num(m,lx,ly,dir1)
        num = n1+n2+1
        if num >= 5:
            return True
    return False 

# isRunning = False
isRunning = True
while isRunning:
    #遍历窗口发生的所有事件
    for event in pygame.event.get():
        #根据事件的类型，进行判断
        #响应关闭窗口事件
        if event.type == pygame.QUIT:
            isRunning = False
        #响应鼠标点击事件
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game_state == 1:
            x,y = event.pos
            xi = round((x-space)/cell_size)
            yi = round((y-space)/cell_size)
            #判断棋子是否落在棋盘内，并且没有重复落子。如果为真，落子，并且切换棋子的颜色
            if xi>=0 and xi<cell_num and yi>=0 and yi<cell_num and (xi,yi,1) not in chess_arr and (xi,yi,2) not in chess_arr:
                chess_arr.append((xi,yi,flag))
                if check_win(chess_arr,flag):
                    game_state = 2 if flag == 1 else 3
                else:
                    flag = 2 if flag == 1 else 1
        #响应键盘事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                chess_arr = []
                flag = 1
                game_state = 1       
        
    screen.fill((0,150,200))
    #画棋盘
    for i in range(0,cell_num):
        grid_font = pygame.font.Font(None,35)
        num_text = str(i)
        num_image = grid_font.render(num_text,False,(100,100,100))
        num_size = num_image.get_size()
        screen.blit(num_image,(space-num_size[0]-16,space+i*cell_size))
        pygame.draw.line(screen,black,(space,space+i*cell_size),(grid_size-space,space+i*cell_size),1)
        screen.blit(num_image,(space+i*cell_size,space-num_size[1]-16))
        pygame.draw.line(screen,black,(space+i*cell_size,space),(space+i*cell_size,grid_size-space),1)

    pygame.draw.circle(screen,black,(space+cell_size*3,space+cell_size*3),3,0)    
    pygame.draw.circle(screen,black,(space+cell_size*3,grid_size-space-cell_size*3),3,0)    
    pygame.draw.circle(screen,black,(grid_size-space-cell_size*3,space+cell_size*3),3,0)    
    pygame.draw.circle(screen,black,(grid_size-space-cell_size*3,grid_size-space-cell_size*3),3,0)    
    pygame.draw.circle(screen,black,(grid_size/2,grid_size/2),5,0)
    pygame.draw.rect(screen,black,[space-4,space-4,cell_size*(cell_num-1)+9,cell_size*(cell_num-1)+9],3)    


    #落子
    for x,y,c in chess_arr:
        chess_color = black if c == 1 else white
        pygame.draw.circle(screen,chess_color,(x*cell_size+space,y*cell_size+space),16,0)

    if game_state!=1:
        myfont = pygame.font.Font(None,100)
        text = "%s WIN!" % ('black' if flag ==1 else 'white')
        text_image = myfont.render(text,False,(100,0,0))
        text_size = text_image.get_size()
        screen.blit(text_image,(grid_size/2-text_size[0]/2,grid_size/2-text_size[1]/2))
    
    pygame.display.update()

pygame.quit()