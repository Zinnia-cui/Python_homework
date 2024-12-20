import math
flag = 1 #1为一般
a, b, c = map(eval,input().split())     #输入三角形三边长，中间用空格分隔，如3 4 5
if a+b > c and b+c > a and a+c > b:
    if round(a,1) == round(b,1) == round(c,1):
        print('等边',end="")
        flag = 0
    elif round(a,1) == round(b,1) or round(b,1) == round(c,1) or round(a,1) == round(c,1):
        print('等腰', end="")
        flag = 0
    if round(a*a+b*b) == round(c*c) or round(a*a+c*c) == round(b*b) or round(b*b+c*c) == round(a*a):
        print('直角',end="")
        flag = 0
    if flag:
        print('一般',end="")
    print('三角形')
else:
    print("不是三角形")

