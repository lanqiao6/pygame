def GetWeekWithDate(y, m, d):
    y = y-1 if m == 1 or m == 2 else y
    m = 13 if m == 1 else (14 if m == 2 else m)
    w = (d+2*m+3*(m+1)//5+y+y//4-y//100+y//400) % 7+1
    return w

def IsLeepYear(y):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        return True
    return False

def GetDaysInMonth(y, m):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if IsLeepYear(y) else 28  

year = int(input("请输入年份："))
month = int(input("请输入月份："))

#year,month = 2019,2

days = GetDaysInMonth(year, month)

print("一 二 三 四 五 六 日")
print("-"*20)

for i in range(1, days+1):
    w = GetWeekWithDate(year, month, i)
    if i == 1:
        print(f"{' ' *(w-1)*3}", end="")
    else:
        if w == 1:
            print("")
    print(f"{i:2d}", end=" ")
print("")
