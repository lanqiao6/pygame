
import random
list1 = [[random.randint(0,1)]*5 for i in range(0,5)]
print(list1)
for y in range(0,5):
    for x in range(0,5):
        print(list1[x][y],end=' ')
    print()
print('=============')

for i in list1:
    for j in i:
        print(j,end=' ')
    print()
print()