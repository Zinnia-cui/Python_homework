'''有一个定义在自然数上的函数 f(x) 定义如下：

                若 x <5 , 则 f(x) = x;

                若 5<=x<15, 则 f(x) = x+6;

                若 x>=15, 则 f(x) = x-6。

试编写该函数，输入x值，输出相应的f(x)值。'''

def f(x):
    if x < 5:
        return x
    elif x < 15:
        return x+6
    else:
        return x-6

def main():
    x=int(input())
    y=f(x)
    print(y)
main()


