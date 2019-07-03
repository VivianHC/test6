# -*- coding: UTF-8 -*-

# Filename : triangle.py
# author by : （Vivian)

print('\n---玩转三角形---')
a=float(input('输入三角形第一边长 a=: '))
b=float(input('输入三角形第二边长 b=: '))
c=float(input('输入三角形第三边长 c=: '))
if(a+b>c)and(a+c>b)and(b+c>a):
    if(abs(a-b)>=c)or(abs(a-c)>=b)(abs(b-c)>=a):
        print("错误！某两边之差大于等于第三边，所以无法组成三角形。")
    else:
        if(a==b)or(a==c)or(b==c):
            print('正确！可以组成等边或等腰三角形。')
        else:
            print('正确！可以组成不等腰三角形。')

else:
    print("错误！某两边之和小于等于第三边，所以无法组成三角形。")
