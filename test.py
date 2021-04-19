
def IsLeepYear(y):
    if y%400 == 0 or (y%4 == 0 and y%100 != 0):
        return True
    return False


def GetDaysInMonth(y,m):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if IsLeepYear(y) else 28

def GetWeekWithDate(y,m,d):
    if m == 1:
        m = 13
        y = y-1
    elif m == 2:
        m = 14
        y = y-1
    else:
        y = y
        m = m
    w = (d+2*m+3*(m+1)//5+y+y//4-y//100+y//400) % 7+1
    return w



y, m = 2021, 4

#y = int(input("请输入年份："))
#m = int(input("请输入月份："))

d = GetDaysInMonth(y,m) 

print('一 二 三 四 五 六 七')
print('=' * 21)

for i in range(1, d+1):
    w=GetWeekWithDate(y,m,i)

    if i == 1:
        print(' '*((w-1)*3), end='')
    print(f'{i:2d}', end=' ')
    if w == 7:
        print()
