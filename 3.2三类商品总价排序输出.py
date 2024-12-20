n1=eval(input('num1:'))
n2=eval(input('num2:'))
n3=eval(input('num3:'))
price1=eval(input('price1:'))
price2=eval(input('price2:'))
price3=eval(input('price3:'))
v1=n1*price1
v2=n2*price2
v3=n3*price3
if v1>v2:
    v1,v2=v2,v1
if v1>v3:
    v1,v3=v3,v1
if v2>v3:
    v2,v3=v3,v2
print('values:$%.2f,$%.2f,$%.2f'%(v1,v2,v3))

num,price = [],[]
d = []
for i in range(3):
    num.append(eval(input('num{:}:'.format(i+1))))
for i in range(3):
    price.append(eval(input('price{:}:'.format(i+1))))
for i in range(3):
    d.append(num[i]*price[i])
d.sorted()
print('values:${0:.2f},${1:.2f},${2:.2f]'.format(d[0],d[1],d[2]))

