# 函数 is_prime(n) 用来判断 n 是否为素数
# 是素数返回 True，否则返回 False
# ############################
def is_prime(n):  #
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 函数 find_next_prime(n) 用来计算并返回大于 n 的最小素数
# 此函数内调用 is_prime(n)
def find_next_prime(n):
    n += 1
    #计算并返回大于 n 的最小素数
    while not is_prime(n):
        n += 1

    return n

def main():
    n = int(input("请输入整数n："))
    print("n是素数：", is_prime(n))
    print("大于n的最小素数为：", find_next_prime(n))


main()