n = input()
if len(n)!=6:
    print("wrong")
elif not n.isdigit():
    print("wrong")
else:
    for i in range(1,6):
        x=int(n[i-1])
        m=(x+1)**3%10
    if int(n[i])==m:
         print("right")
    else:
         print("wrong")

