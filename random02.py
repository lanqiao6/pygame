
import random

def pc_round():
    l = []
    for i in range(0,3):
        r = random.randint(1, 6)
        l.append(r)
    return sum(l)


#1、用户注册，分配金币，打印游戏提示信息；
##用户注册。定义一个字典，存储用户信息，name，age
user_info = {}
name = input('请填写用户名：')
age = int(input('{} 您好，请输入您的年龄：'.format(name)))
user_info = {'name':name,'age':age}
##分配金币,10到18s
if 10<=age<18:
    gold = 1000
elif 18<=age<30:
    gold = 1500
else:
    gold = 500
user_info['gold'] = gold
#打印欢迎信息
print("{} 您好，欢迎玩本游戏，您的初始金币为：{}".format(user_info['name'],
                                           user_info['gold']))
##打印游戏提示信息
# print('{:*^53}'.format('游戏说明'))
print('游戏说明'.center(53,'*'))
print('*'.ljust(55),'*')    
print('*','电脑每次投掷3枚骰子，总点数≥10为大，否则为小'.center(33),'*')
print('*'.ljust(55),'*')  
print(''.center(57,'*'))

#2、开始猜测，猜测大小，判断输赢，显示现有金币
while True:
    print('开始猜大小'.center(52,'-'))
    pc_size = 'big' if pc_round()>=10 else 'small'
    user_size = input('请输入big or small：')
    if pc_size == user_size:
        print('您赢了！')
        user_info['gold'] += 100
    else:
        print('您输了！')
        user_info['gold'] -= 100
    print('您现有金币：{}'.format(user_info['gold']))
    if user_info['gold']<=0:
        print('您的金币已经用完，感谢您的使用')
        break
print('欢迎下次来玩，再见!')











