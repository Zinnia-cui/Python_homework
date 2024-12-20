year,k = map(int,input().split(','))
def is_leap(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
count = 0
for i in range(year,year+k+1):
    if is_leap(i):
        print(f'{i:>6}',end='')
        count+=1
        if count%4==0:
            print()

