#! /usr/bin/python3

"""
将华氏温度转化成摄氏温度
提示：华氏温度到摄氏温度的转换公式为：C = (F-32)/1.8
"""
f = float(input('请输入华氏温度：'))
c = (f-32)/1.8
print('%.1f华氏温度 = %.1f摄氏温度' %(f, c))