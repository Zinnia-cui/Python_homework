total = 0    # 总和
count1 = 0  # 正数个数
count2 = 0  # 负数个数
num = int(input())  # 从键盘输入一个整数
while num!= 0:
    if num > 0:
        count1 += 1  # 统计正数个数
    elif num < 0:
        count2 += 1  # 统计负数个数
    total += num  # 累加总和
    num = int(input())
# 输出结果
average = total / (count1 + count2)  # 计算平均值
print(f"{average:.1f}")  # 输出平均值，保留两位小数
print(count1)     # 输出正数个数
print(count2)     # 输出负数个数


