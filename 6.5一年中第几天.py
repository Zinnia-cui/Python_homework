# 计算给定日期是该年份的第多少天
n=list(map(int,input().split()))
year=n[0]
month=n[1]
day=n[2]
days=[31,28,31,30,31,30,31,31,30,31,30,31]
if (year%4==0 and year%100!=0) or year%400==0:
    days[1]=29
sum = 0
# 累加到指定月份的天数
for i in range(month-1):
    sum+=days[i]
sum+=day
# 输出结果
print(sum)


