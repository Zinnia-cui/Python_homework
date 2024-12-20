def is_prime(n): #
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 打印2到1000之间的素数
print()
count = 0
for num in range(2, 1001):
    if is_prime(num):
        print(f"{num:>4}", end='')
        count += 1
        if count % 10 == 0:  # 每10个素数换行
            print()



