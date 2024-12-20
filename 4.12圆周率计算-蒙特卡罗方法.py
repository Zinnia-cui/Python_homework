#圆周率计算-蒙特卡罗方法
import random
random.seed(0)   # 设置初始化随机数种子为0
n=int(input())
count=0
for i in range(n):
    x=random.random()#获得一个0~1之间的随机小数
    y=random.random()
    if(x**2+y**2)<=1:
        count+=1
pi=4*(count/n)
print(pi)

