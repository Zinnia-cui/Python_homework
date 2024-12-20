count=0
for i in range(100, 1000):
    if i % 10 == 5 and i % 3 == 0:
        print(i, end='#')
        count += 1
        if count%8==0:
            print()

