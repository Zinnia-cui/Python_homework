a=eval(input('Enter an integer:'))
n1=a//1000
n2=(a-n1*1000)//100
n3=(a-n1*1000-n2*100)//10
n4=a%10
b=n4*1000+n3*100+n2*10+n1
print('The reversed number is',b)

