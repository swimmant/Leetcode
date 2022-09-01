# 输入包括两个正整数a,b(1 <= a, b <= 1000),输入数据包括多组。
# 1 5
# 10 20
while True:
    try:
        a,b = map(int,input().split(" "))
        print(a+b);
    except:
        break;

# 输入第一行包括一个数据组数t(1 <= t <= 100)
# 接下来每行包括两个正整数a,b(1 <= a, b <= 1000)
# 输出a+b的结果
# 2
# 1 5
# 10 20

t= int(input())
for i in range(t):
    print(sum(map(int,input().split(" "))))

# 输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据有多组, 如果输入为0 0则结束输入
# 输出a+b的结果

# 2 5
# 1 5
# 0 0

ab = input()
while(ab != "0 0"):
    print(sum(map(int,ab.split(" "))))
    ab = input()

# 计算一系列数的和
# 输入数据包括多组。
# 每组数据一行,每行的第一个整数为整数的个数n(1 <= n <= 100), n为0的时候结束输入。
# 接下来n个正整数,即需要求和的每个正整数。

# 4 1 2 3 4
# 5 1 2 3 4 5
# 0


ab = input()
while ab != '0':
    l1 = list(map(int,ab.split(" ")))[1:]
    sum =0
    for i in l1:
        sum+= i
    print(sum)
    ab = input()

# 输入的第一行包括一个正整数t(1 <= t <= 100), 表示数据组数。
# # 接下来t行, 每行一组数据。
# # 每行的第一个整数为整数的个数n(1 <= n <= 100)。
# # 接下来n个正整数, 即需要求和的每个正整数。
# 每组数据输出求和的结果

# 2
# 4 1 2 3 4
# 5 1 2 3 4 5

# 10
# 15

ab = int(input())
i = 0
while i < ab :
    l1 = list(map(int,input().split(" ")))[1:]
    print(sum(l1))
    i += 1


# 输入数据有多组, 每行表示一组输入数据。
# 每行的第一个整数为整数的个数n(1 <= n <= 100)。
# 接下来n个正整数, 即需要求和的每个正整数。
# 每组数据输出求和的结果
# 4 1 2 3 4
# 5 1 2 3 4 5

# 10
# 15

while True:
    try:
        ab = map(int,input().split(" "))
        l1 = list(ab)[1:]
        print(sum(l1))
    except:
        break

# 输入数据有多组, 每行表示一组输入数据。
#
# 每行不定有n个整数，空格隔开。(1 <= n <= 100)。

# 每组数据输出求和的结果

# 1 2 3
# 4 5
# 0 0 0 0 0

# 6
# 9
# 0

while True:
    try:
        ab = map(int,input().split(" "))
        l1 = list(ab)
        print(sum(l1))
    except:
        break

