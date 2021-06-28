#import time
import random

#存储用户购买的道具
user_properties = {}
#定义道具种类，
properties = {'0-X3-(100金币)', '1-X5-(200金币)'}
#定义一个字典，用于存储用户信息name，age，glod
user_info = {}


def register():
    '''
    用户注册，分配金币，打印游戏开始的提示信息
    '''
    #引用全局变量，存储用户注册信息
    global user_info
    name = input('请填写用户名：')
    age = input('{} 您好，请输入您的年龄：'.format(name))
    user_info = {'name': name, 'age': int(age)}
    #如果年龄在10-18岁初始金币1000，如果年龄在18-30岁初始金币1500，其他年龄初始金币500.
    if 10 <= user_info['age'] < 18:
        glod = 1000
    elif 18 <= user_info['age'] < 30:
        glod = 1500
    else:
        glod = 500
    user_info['glod'] = glod
    #打印游戏开始的提示信息
    print("{} 您好，欢迎玩本游戏，您的初始金币为：{}".format(user_info['name'],
                                           user_info['glod']))
    #time.sleep(1)
    print('游戏说明'.center(50, '*'))
    print('*'.ljust(52), '*')
    print('*', end='')
    print("电脑每次投掷3枚骰子，总点数≥10为大，否则为小".center(32), end='')
    print('*')
    print('*'.ljust(52), '*')
    print('*' * 54)


def start_guess():
    '''
    打印开始猜测的提示信息，产生随机数，猜测大小
    '''
    print('---------------------开始猜大小---------------------')
    dices = []
    for i in range(0, 3):
        dices.append(random.randint(1, 6))
    s = sum(dices)
    user_input = input('请输入big or small ：')
    u = user_input.strip().lower()
    #time.sleep(0.5)
    return s, u


def use_props():
    #定义变量，存储金币翻倍的倍数
    multi = 1
    #如果用户有道具，提示是否使用道具
    if len(user_properties) > 0:
        use_pro = input('是否使用道具 yes or no：')
        #如果用户使用了道具，删除该道具，金币翻倍
        if use_pro.lower() == 'yes':
            use_pro = int(input('请选择使用第几个道具{}：'.format(user_properties)))
            if user_properties[str(use_pro)] == False:
                print('输入错误，本次不使用道具！')
                return 1
            if user_properties[str(use_pro)] == 'X3':
                multi = 3
                print('奖金翻3倍,')
            elif user_properties[str(use_pro)] == 'X5':
                multi = 5
                print('奖金翻5倍,'.format(multi))
            #删除用户使用的道具
            del user_properties[str(use_pro)]
    return multi


def win_or_loss(multi, s, u):
    if (s >= 10 and u == 'big') or (s < 10 and u == 'small'):
        print('您赢了！！！')
        user_info['glod'] += (100 * multi)
        print('您现在有金币：{}'.format(user_info['glod']))
    else:
        print('您输了！')
        user_info['glod'] -= (100 * multi)
        print('您现在有金币：{}'.format(user_info['glod']))
    if (user_info['glod'] <= 0):
        print('您的金币已经用完，感谢您的使用')
        return 0
    else:
        return 1


def buy_props():
    #如果金币是400的倍数，提示是否购买道具
    if user_info['glod'] % 400 == 0:
        shop = input('您现在有金币：{},是否购买道具 yes or no: '.format(user_info['glod']))
        if shop.lower() == 'yes':
            #选择要购买的道具，存储用户道具，扣除金币
            good_num = input('请选择要购买第几个道具{}：'.format(properties))
            if good_num == '0':
                user_properties[str(len(user_properties))] = 'X3'
                user_info['glod'] -= 100
                print('购买成功！消耗金币100')
                print('您现有金币：{}'.format(user_info['glod']))
            elif good_num == '1':
                user_properties[str(len(user_properties))] = 'X5'
                user_info['glod'] -= 200
                print('购买成功！消耗金币200')
                print('您现有金币：{}'.format(user_info['glod']))
            else:
                print('没有该道具，您失去了这次机会')
        else:
            #打印剩余的金币
            print('您现有金币：{}'.format(user_info['glod']))


if __name__ == '__main__':
    register()
    while True:
        s, u = start_guess()
        multi = use_props()
        if (win_or_loss(multi, s, u) == 0):
            break
        buy_props()
    print('欢迎下次来玩，再见！')