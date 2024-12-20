#Fib数列计算
'''
m=eval(input())
n=eval(input())
# 定义函数
def fib(i): # 一个整数数列，它的第一项是m，第二项是n，以后每项都是前两项之和。
    if i == 0:
        return m
    elif i == 1:
        return n
    else:
        return fib(i-1) + fib(i-2)
if type(m) is float or type(n) is float:
    print('illegal input')
else:
    sum = 0
    for i in range(20):
        sum += fib(i)
    print(sum)'''

# 优化
m=eval(input())
n=eval(input())
if isinstance(m, int)==False or isinstance(n, int)==False:
    print('illegal input')
else:
    lst = [m, n]
    for i in range(18):
        s = lst[i] + lst[i+1]
        lst.append(s)
    print(sum(lst))



