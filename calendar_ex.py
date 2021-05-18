

# 光标移动的方向
Direction_Up = 0    # 上
Direction_Down = 1  # 下
Direction_Left = 2  # 左
Direction_Right = 3 # 右
# 字体颜色和背景色
Color_Normal = -1       # 默认色
Color_Black = 0         # 黑色
Color_Red = 1           # 红色
Color_Green = 2         # 绿色
Color_Yellow = 3        # 黄色
Color_Blue = 4          # 蓝色
Color_Purple = 5        # 紫色
Color_Green_Dark = 6    # 深绿色
Color_White = 7         # 白色

def set_pointer_pos(x, y):
    ''' 设置光标位置, 控制台左上角的坐标位置是 (1, 1) '''
    print(f'\33[{y};{x}H', end='')

def clean(should_restart=True):
    '''
    清空控制台\n
    should_restart: 是否将光标重置到左上角
    '''
    print('\33[2J', end='')
    if should_restart:
        set_pointer_pos(1, 1)

def clean_to_end():
    ''' 删除光标当前位置到行尾的所有内容 '''
    print('\33[K', end='')

def save_pointer_pos():
    ''' 保存光标当前位置 '''
    print('\33[s', end='')

def load_pointer_pos():
    ''' 恢复光标到上一次保存的位置 '''
    print('\33[u', end='')

def show_pointer(should_show):
    ''' 显示/隐藏光标 '''
    print('\33[?25' + ('h' if should_show else 'l'), end='')

def move_pointer(direction, distance):
    '''
    移动光标位置\n
    direction: 移动的方向, 上/下/左/右\n
    distance: 移动的距离
    '''
    if direction == Direction_Up:
        print(f'\33[{distance}A', end='')
    elif direction == Direction_Down:
        print(f'\33[{distance}B', end='')
    elif direction == Direction_Right:
        print(f'\33[{distance}C', end='')
    else:
        print(f'\33[{distance}D', end='')

def print_style(text, color=Color_Normal, bg_color=Color_Normal, bold=False, underline=False, invert=False, hide=False, end='\n'):
    '''
    按照指定样式打印文本内容\n
    color: 字体颜色\n
    bg_color: 背景色\n
    bold: 文字加粗\n
    underline: 下划线\n
    invert: 颜色和背景色反显\n
    hide: 隐藏文本内容\n
    end: 结束符, 默认为换行
    '''
    s = f'\33[{30 + color}m' if color != Color_Normal else ''
    s += f'\33[{40 + bg_color}m' if bg_color != Color_Normal else ''
    s += '\33[1m' if bold else ''
    s += '\33[4m' if underline else ''
    s += '\33[7m' if invert else ''
    s += '\33[8m' if hide else ''
    s += text + '\33[0m'
    print(s, end=end)

''' ↓↓↓↓↓↓ 下边是测试代码 ↓↓↓↓↓↓ '''
is_exit = False
content = 'Hello'
is_bold = False
is_underline = False
is_invert = False
is_hide = False
color = Color_Normal
bg_color = Color_Normal
while not is_exit:
    clean()
    show_pointer(False)
    print('A. 改变文本内容')
    print('B. 改变文本颜色')
    print('C. 改变背景颜色')
    print('D. 加粗 / 不加粗')
    print('E. 显示 / 取消 下划线')
    print('F. 颜色反显')
    print('G. 隐藏 / 显示')
    print('Q. 退出程序')
    save_pointer_pos()
    count = len(content)
    set_pointer_pos(30, 4)
    print(f'╔{"═" * (count + 2)}╗', end='')
    set_pointer_pos(30, 5)
    print(f'║{" " * (count + 2)}║', end='')
    set_pointer_pos(30, 6)
    print(f'╚{"═" * (count + 2)}╝', end='')
    set_pointer_pos(32, 5)
    print_style(content, color, bg_color, is_bold, is_underline, is_invert, is_hide, '')
    load_pointer_pos()
    command = input('请输入命令: ').lower()
    if command == 'q':
        clean()
        show_pointer(True)
        is_exit = True
    elif command == 'a':
        i = input('请输入新的文本内容: ')
        content = i
    elif command == 'b':
        print('0. 默认, 1. 黑, 2. 红, 3. 绿, 4. 黄, 5. 蓝, 6. 紫, 7. 深绿, 8. 白')
        i = input('请设置文本颜色: ')
        i = int(i)
        color = i - 1
    elif command == 'c':
        print('0. 默认, 1. 黑, 2. 红, 3. 绿, 4. 黄, 5. 蓝, 6. 紫, 7. 深绿, 8. 白')
        i = input('请设置背景颜色: ')
        i = int(i)
        bg_color = i - 1
    elif command == 'd':
        is_bold = not is_bold
    elif command == 'e':
        is_underline = not is_underline
    elif command == 'f':
        is_invert = not is_invert
    elif command == 'g':
        is_hide = not is_hide
