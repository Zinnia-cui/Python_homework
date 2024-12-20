money = int(input())
count = 0
for n10 in range(money // 10 + 1):
    for n5 in range(money // 5 + 1):
        for n2 in range(money // 2 + 1):
            if n10 * 10 + n5 * 5 + n2 * 2 == money:
                count += 1
                print(('{0:<4d}{1:<4d}{2:<4d}'.format(n10, n5, n2)))
print(count)

