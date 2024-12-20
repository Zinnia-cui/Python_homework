n=eval(input())
f1,f2=1,1
print("{:10}".format(f1), end="")
print("{:10}".format(f2), end="")
t=2
for i in range(2,n):
    f3=f1+f2
    print("{:10}".format(f3), end="")
    t+=1
    if (t%6==0):
        print()
    f1=f2
    f2=f3

