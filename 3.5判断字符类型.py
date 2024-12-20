a=input()
b=ord(a)
#0-48,9-57,A-65,Z-90,a-97,z-122
if 48<=b<=57:
    print("numeric")
elif 65<=b<=90 or 97<=b<=122:
    print("alpha")
else:
    print("other")

