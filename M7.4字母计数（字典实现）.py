article= input()
a=article
count_article={}
counts=count_article
n=0
for i in a:
    if i.isalpha():
        if i in counts:
            counts[i]+=1
        else:
            counts[i]=1
x=max(counts.values())
for i in sorted(counts):
    if counts[i]==x:
        n+=1
        print('{}:{}'.format(i,counts[i]),end=' ')
        if n==5:
            print()



