import math
a,b,c = map(float,input().split())
deta = b * b - 4 * a * c
if deta<0:
    print('No')
elif deta==0:
    x = - (b / 2*a)
    print('%.2f %.2f'%(x,x))
else:
    x1 = (-b + math.sqrt(deta)) / (2 * a)
    x2 = (-b - math.sqrt(deta)) / (2 * a)
    print('%.2f %.2f'%(x1,x2))






