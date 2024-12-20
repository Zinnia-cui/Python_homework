a=input()
print(a.split('\\'))
print(a.replace('\\','/'))
x=len(a)
b=a.count('\\',0,x)
print(x,b,sep=':')


