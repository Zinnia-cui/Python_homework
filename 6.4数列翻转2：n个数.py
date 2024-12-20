n=input()
a=list(map(int,n.split()))
s=a.pop(0)
#del a[0]
a.reverse()
print(' '.join(map(str, a)))

'''lst = []
lst = list(input().strip().split())
n = int(lst[0])
for i in range(n, 0, -1):
    print(lst[i], end=' ')'''


