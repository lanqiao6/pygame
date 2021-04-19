

def getDayWithMonth(y,m):
    '''获取一个月的天数'''
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    else:
        if y%400 == 0 or (y%4 == 0 and y%exit100 != 0):
            return 29
        else:
            return 28
 

#1、接受用户输入年，月
year = int(input('请输入年份'))
month = int(input('请输入月份'))

#2、根据年月，计算这个月总共有多少天
day = getDayWithMonth(year,month)
print(day)


#3、按照格式打印结果


print('一 二 三 四 五 六 日')
print('-'*20)

