#! /usr/bin/python3

import random

# 随机产生一个1-100的随机整数
answer = random.randint(1, 100)

# 制定计数器
counter = 0

while True:
    counter += 1
    numner = int(input('请输入: '))
    if numner < answer:
        print('大一点')
    elif numner > answer:
        print('小一点')
    else:
        print('恭喜你猜对了！')
        break
print(f'你总共猜了{counter}次')