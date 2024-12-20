
year=eval(input())
x=166.37*10**8
x1=38241*365*24*year+x
x2=x1*1.609344
x3=x1/92955887.6
v=299792.458*3600
time=x2*2/v
print("distance:")
print("%.2f %s"%(x1,'miles'))
print("%.2f %s"%(x2,'km'))
print("%.2f %s"%(x3,'AU'))
print("%s %.2f %s"%('time:',time,'hours'))


