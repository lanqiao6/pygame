import random


#1、用户注册，分配金币，打印游戏提示信息；
def user_in():
    global user_info
    name = input('请填写用户名：')
    age = int(input('{} 您好，请输入您的年龄：'.format(name)))
    user_info = {'name': name, 'age': age}
    ##分配金币,10到18s
    if 10 <= age < 18:
        gold = 1000
    elif 18 <= age < 30:
        gold = 1500
    else:
        gold = 500
    user_info['gold'] = gold
    #打印欢迎信息
    print("{} 您好，欢迎玩本游戏，您的初始金币为：{}".format(user_info['name'],
                                           user_info['gold']))
    ##打印游戏提示信息
    # print('{:*^53}'.format('游戏说明'))
    print('游戏说明'.center(53, '*'))
    print('*'.ljust(55), '*')
    print('*', '电脑每次投掷3枚骰子，总点数≥10为大，否则为小'.center(33), '*')
    print('*'.ljust(55), '*')
    print(''.center(57, '*'))


def pc_round():
    l = []
    for i in range(0, 3):
        r = random.randint(1, 6)
        l.append(r)
    return sum(l)


def start_guess():
    ##提示开始猜测
    print('开始猜大小'.center(52, '-'))
    ##获取电脑随机结构，big or small
    pc_size = 'big' if pc_round() >= 10 else 'small'
    ##用户猜测
    user_size = input('请输入big or small：')
    return pc_size, user_size


def win_or_loss(pc_size, user_size, multi):
    if pc_size == user_size:
        print('您赢了！')
        user_info['gold'] += 100 * multi
    else:
        print('您输了！')
        user_info['gold'] -= 100 * multi
    log_gold.append(user_info['gold'])
    print('您现有金币：{}'.format(user_info['gold']))


def buy_props(r):
    if user_info['gold'] % 400 == 0:
        shop = input('您现在有金币：{},是否购买道具 yes or no:'.format(user_info['gold']))
        if shop.lower() == 'yes':
            c = input('请选择要购买第几个道具{}:'.format(properties))
            if c == '0':
                user_properties[r] = 'X3'
                user_info['gold'] -= 100
                print('购买成功！消耗金币100')
            elif c == '1':
                user_properties[r] = 'X5'
                user_info['gold'] -= 200
                print('购买成功！消耗金币200')
            else:
                print('没有该道具，您失去了这次机会')
        print('您现有金币：{}'.format(user_info['gold']))


def use_props():
    multi = 1
    if len(user_properties) > 0:
        u = input('是否使用道具 yes or no：')
        if u.lower() == 'yes':
            c = int(input('请选择使用第几个道具{}:'.format(user_properties)))
            if user_properties[c] == False:
                print('输入错误，本次不使用道具！')
                return 1
            elif user_properties[c] == 'X3':
                multi = 3
                print('奖金翻3倍')
            elif user_properties[c] == 'X5':
                multi = 5
                print('奖金翻5倍')
            del user_properties[c]
    return multi


#定义道具种类，
properties = {'0-X3-(100金币)', '1-X5-(200金币)'}
#存储用户购买的道具
user_properties = {}
##定义一个字典，存储用户信息，name，age
user_info = {}
log_gold = []

#用户登录
user_in()

r = 0

#2、开始猜测，猜测大小，判断输赢，显示现有金币
while True:
    r += 1
    ##猜测大小
    ps, us = start_guess()
    #使用道具
    multi = use_props()
    ##判断输赢，显示现有金币
    win_or_loss(ps, us, multi)
    ##如果金币小于或等于0，退出游戏
    if user_info['gold'] <= 0:
        print('您的金币已经用完，感谢您的使用')
        break
    ##购买道具
    buy_props(r)
log_gold.sort(reverse=True)
print('欢迎下次来玩，再见！最高金币：{}'.format(log_gold[0]))
