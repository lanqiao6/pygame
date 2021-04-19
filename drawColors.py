# 文件名: drawFranceFlag.py

# 导入Pygame
import pygame
from pygame.color import THECOLORS

# 初始化
pygame.init()

# 生成一个窗口
screen = pygame.display.set_mode([800, 500])

# 将白色铺满整个窗口
screen.fill(THECOLORS['white'])


# 添加蓝色与红色区域
pygame.draw.rect(screen, THECOLORS['black'], [0, 0, 800, 100], 0)
pygame.draw.rect(screen, THECOLORS['white'], [0, 100, 800, 200], 0)
pygame.draw.rect(screen, THECOLORS['red'], [0, 200, 800, 300], 0)
pygame.draw.rect(screen, THECOLORS['green'], [0, 300, 800, 400], 0)
pygame.draw.rect(screen, THECOLORS['blue'], [0, 400, 800, 500], 0)

# 翻转
pygame.display.flip()

# 主循环&保存
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(screen, 'Colors.jpg')
            mRunning = False
pygame.quit()
