#! /usr/bin/python3

"""
输入半径计算圆的周长和面积
C=2rd
area = 3.1416*r*r
"""
radius = float(input("请输入圆的半径:"))
perimeter = 2 * 3.1416 *radius
area = 3.1416 * radius *radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)